'use strict';
/* 行政書士 過去問演習アプリ — vanilla JS, データは exam.json / oneliner.json */

/* ---------- Firebase 設定 ---------- */
// Firebase コンソール → プロジェクト設定 → マイアプリ → SDK の設定と構成 から取得
const firebaseConfig = {
  apiKey:           'AIzaSyAq30YknuAEwiL6QlYXINIZgStxquILCM4',
  authDomain:       'gyosei-kakomon.firebaseapp.com',
  projectId:        'gyosei-kakomon',
};
firebase.initializeApp(firebaseConfig);
const fbAuth = firebase.auth();
const fbDb   = firebase.firestore();
const EMAIL_KEY = 'gyosei_email_for_signin';

const $ = (s) => document.querySelector(s);
const PROGRESS_KEY = 'gyosei_progress_v1';

const state = {
  mode: 'oneliner',          // 'oneliner' | 'exam'
  oneliner: [],
  exam: [],
  queue: [],
  idx: 0,
  answered: false,
  session: { correct: 0, wrong: 0, results: [] },
};

/* ---------- 進捗(localStorage) ---------- */
function loadProgress() {
  try { return JSON.parse(localStorage.getItem(PROGRESS_KEY)) || {}; }
  catch { return {}; }
}
function saveProgress(p) { localStorage.setItem(PROGRESS_KEY, JSON.stringify(p)); }
function recordResult(id, ok) {
  const p = loadProgress();
  const r = p[id] || { correct: 0, wrong: 0 };
  if (ok) r.correct++; else r.wrong++;
  r.last = ok ? 'o' : 'x';
  p[id] = r;
  saveProgress(p);
  // 同期は applySrs 側で interval/due を含めて一括で行う
}

/* ---------- 間隔反復(忘却曲線) ---------- */
// 間違えた問題を「忘れた頃」に自動で再出題する。
// × → 翌日 / △(あいまい) → 短め / ○ → 前回間隔×2.5 で間隔を広げる。
function todayStr(d) {
  d = d || new Date();
  const m = String(d.getMonth() + 1).padStart(2, '0');
  const day = String(d.getDate()).padStart(2, '0');
  return `${d.getFullYear()}-${m}-${day}`;
}
function addDaysStr(days) {
  const d = new Date();
  d.setDate(d.getDate() + days);
  return todayStr(d);
}
function applySrs(id, rating, base) {
  const p = loadProgress();
  const r = p[id];
  if (!r) return;
  let interval;
  if (rating === 'again') interval = 1;
  else if (rating === 'hard') interval = base > 0 ? Math.max(1, Math.round(base * 1.3)) : 1;
  else interval = base > 0 ? Math.round(base * 2.5) : 1; // good
  r.interval = interval;
  r.due = addDaysStr(interval);
  p[id] = r;
  saveProgress(p);
  syncResult(id); // interval/due を含めて Firestore へ
}
function dueQuestions() {
  const p = loadProgress();
  const today = todayStr();
  const all = state.oneliner.concat(state.exam);
  return all
    .filter((q) => { const r = p[q.id]; return r && r.due && r.due <= today; })
    .sort((a, b) => (p[a.id].due < p[b.id].due ? -1 : 1));
}
function srsLabel(due) {
  if (!due) return '—';
  const days = Math.round((new Date(due) - new Date(todayStr())) / 86400000);
  if (days <= 0) return '今日';
  if (days === 1) return '明日';
  return `${days}日後`;
}
function updateReviewCard() {
  const n = dueQuestions().length;
  const card = document.getElementById('reviewCard');
  if (!card) return;
  document.getElementById('dueCount').textContent = n;
  card.hidden = n === 0;
}
const REVIEW_CAP = 20; // 1セッションの復習上限（溜まり過ぎても一度に出し過ぎない）
function startReview() {
  const due = dueQuestions();
  if (!due.length) {
    alert('今日の復習はまだありません。問題を解くと、忘れた頃に自動で出題されます。');
    return;
  }
  state.queue = due.slice(0, REVIEW_CAP);
  state.idx = 0;
  state.review = true;
  state.session = { correct: 0, wrong: 0, results: [] };
  show('quiz');
  renderQuestion();
}

/* ---------- 学習記録(時間・継続・計画進捗) ---------- */
const STUDYLOG_KEY = 'gyosei_studylog_v1';
const TARGET_HOURS = 408;          // 計画の総目標時間
const WEEK_TARGET_MIN = 20 * 60;   // 週20時間
// 計画の5フェーズ(日付境界)
const PHASES = [
  { name: '①インプット', start: '2026-06-18', end: '2026-07-31', hours: 126 },
  { name: '②アウトプット', start: '2026-08-01', end: '2026-08-31', hours: 88 },
  { name: '③演習＋記述', start: '2026-09-01', end: '2026-09-30', hours: 86 },
  { name: '④仕上げ', start: '2026-10-01', end: '2026-10-31', hours: 88 },
  { name: '⑤直前', start: '2026-11-01', end: '2026-11-08', hours: 22 },
];

function loadStudyLog() {
  try { return JSON.parse(localStorage.getItem(STUDYLOG_KEY)) || {}; }
  catch { return {}; }
}
function saveStudyLog(o) { localStorage.setItem(STUDYLOG_KEY, JSON.stringify(o)); }

function todayTargetMin() {
  const dow = new Date().getDay(); // 0=日,6=土
  return (dow === 0 || dow === 6) ? 150 : 180;
}
// 学習時間を加算(ボタン)。負値で補正可。0未満にはしない。
function addStudyMinutes(delta) {
  const log = loadStudyLog();
  const d = todayStr();
  const e = log[d] || { min: 0, ans: 0 };
  e.min = Math.max(0, (e.min || 0) + delta);
  log[d] = e;
  saveStudyLog(log);
  syncStudyLog(d);
  renderLog();
}
// 採点時に「今日解いた問題数」を+1(自動・学習日の証跡)
function bumpAnswered() {
  const log = loadStudyLog();
  const d = todayStr();
  const e = log[d] || { min: 0, ans: 0 };
  e.ans = (e.ans || 0) + 1;
  log[d] = e;
  saveStudyLog(log);
}
function isStudied(ds) {
  const e = loadStudyLog()[ds];
  return !!e && ((e.min || 0) > 0 || (e.ans || 0) > 0);
}
// 連続学習日数(今日未着手でも昨日までの連続は維持)
function studyStreak() {
  const d = new Date();
  if (!isStudied(todayStr(d))) d.setDate(d.getDate() - 1);
  let n = 0;
  while (isStudied(todayStr(d))) { n++; d.setDate(d.getDate() - 1); }
  return n;
}
// 今週(月曜起点)の合計分
function weekMinutes() {
  const log = loadStudyLog();
  const now = new Date();
  const dowMon = (now.getDay() + 6) % 7; // 月=0
  let total = 0;
  for (let i = 0; i <= dowMon; i++) {
    const d = new Date(); d.setDate(now.getDate() - i);
    const e = log[todayStr(d)];
    if (e) total += e.min || 0;
  }
  return total;
}
function totalMinutes() {
  return Object.values(loadStudyLog()).reduce((s, e) => s + (e.min || 0), 0);
}
function currentPhase() {
  const t = todayStr();
  return PHASES.find((p) => t >= p.start && t <= p.end)
    || (t < PHASES[0].start ? PHASES[0] : PHASES[PHASES.length - 1]);
}
// 直近5週間(35日)のヒートマップ用セル
function calendarCells() {
  const log = loadStudyLog();
  const today = new Date();
  const dowMon = (today.getDay() + 6) % 7;
  const start = new Date();
  start.setDate(today.getDate() - dowMon - 28); // 4週前の月曜 → 当週まで5週
  const tStr = todayStr(today);
  const cells = [];
  for (let i = 0; i < 35; i++) {
    const d = new Date(start); d.setDate(start.getDate() + i);
    const ds = todayStr(d);
    const e = log[ds];
    const m = e ? (e.min || 0) : 0;
    const ans = e ? (e.ans || 0) : 0;
    let lv = 0;
    if (m >= 180) lv = 4; else if (m >= 120) lv = 3; else if (m >= 60) lv = 2;
    else if (m > 0 || ans > 0) lv = 1; // 時間ログがなくても問題を解いた日は色付け
    cells.push({ ds, lv, future: ds > tStr });
  }
  return cells;
}
function fmtH(min) {
  return (min / 60).toFixed(min % 60 ? 1 : 0);
}
function renderLog() {
  const log = loadStudyLog();
  const today = log[todayStr()] || { min: 0, ans: 0 };
  const target = todayTargetMin();
  const pct = Math.min(100, Math.round(((today.min || 0) / target) * 100));
  const set = (id, v) => { const el = document.getElementById(id); if (el) el.textContent = v; };
  set('logTodayMin', today.min || 0);
  set('logTodayTarget', target);
  set('logTodayAns', today.ans || 0);
  const bar = document.getElementById('logTodayBar');
  if (bar) bar.style.width = pct + '%';
  set('logStreak', studyStreak());
  set('logWeek', fmtH(weekMinutes()) + 'h');
  const total = totalMinutes();
  set('logTotal', fmtH(total) + 'h');
  const ph = currentPhase();
  set('logPhase', `現在: ${ph.name}（〜${ph.end.slice(5).replace('-', '/')}）｜累計 ${fmtH(total)} / ${TARGET_HOURS}h`);
  const cal = document.getElementById('logCal');
  if (cal) {
    cal.innerHTML = calendarCells()
      .map((c) => `<span class="cal-cell lv${c.lv}${c.future ? ' future' : ''}" title="${c.ds}"></span>`)
      .join('');
  }
}

/* ---------- データ ---------- */
async function loadData() {
  const [exam, oneliner] = await Promise.all([
    fetch('data/exam.json').then((r) => r.json()),
    fetch('data/oneliner.json').then((r) => r.json()),
  ]);
  state.exam = exam.map((q) => ({ ...q, __ol: false }));
  state.oneliner = oneliner.map((q, i) => ({ ...q, id: q.id ?? `OL-${i + 1}`, __ol: true }));
}

function currentPool() {
  return state.mode === 'exam' ? state.exam : state.oneliner;
}

/* ---------- ホーム ---------- */
function setMode(mode) {
  state.mode = mode;
  document.querySelectorAll('.mode-card').forEach((b) =>
    b.classList.toggle('active', b.dataset.mode === mode));
  $('#yearWrap').hidden = mode !== 'exam';
  buildFilters();
  updatePoolInfo();
}

function buildFilters() {
  const pool = currentPool();
  const subjects = [...new Set(pool.map((q) => q.subject))].filter(Boolean);
  const subSel = $('#fSubject');
  subSel.innerHTML = '<option value="">すべて</option>' +
    subjects.map((s) => `<option value="${s}">${s}</option>`).join('');
  if (state.mode === 'exam') {
    const years = [...new Set(state.exam.map((q) => q.yearLabel))];
    $('#fYear').innerHTML = '<option value="">すべて</option>' +
      years.map((y) => `<option value="${y}">${y}</option>`).join('');
  }
}

function buildQueue() {
  let pool = currentPool().slice();
  const subj = $('#fSubject').value;
  const year = $('#fYear').value;
  const scope = $('#fScope').value;
  const order = $('#fOrder').value;
  const count = parseInt($('#fCount').value, 10);
  const prog = loadProgress();

  if (subj) pool = pool.filter((q) => q.subject === subj);
  if (state.mode === 'exam' && year) pool = pool.filter((q) => q.yearLabel === year);
  if (scope === 'unseen') pool = pool.filter((q) => !prog[q.id]);
  if (scope === 'wrong') pool = pool.filter((q) => prog[q.id]?.last === 'x');

  if (order === 'shuffle') shuffle(pool);
  else pool.sort((a, b) => (a.seq ?? a.id) > (b.seq ?? b.id) ? 1 : -1);

  if (count > 0) pool = pool.slice(0, count);
  return pool;
}

function shuffle(a) {
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
}

function updatePoolInfo() {
  const n = buildQueue().length;
  $('#poolInfo').textContent = `この条件で ${n} 問`;
}

function renderStats() {
  const prog = loadProgress();
  const ids = Object.keys(prog);
  let c = 0, w = 0;
  ids.forEach((id) => { c += prog[id].correct; w += prog[id].wrong; });
  const total = c + w;
  const acc = total ? Math.round((c / total) * 100) : 0;
  $('#statsBox').innerHTML = `
    <div class="stat"><span class="v">${ids.length}</span><span class="k">挑戦した問題</span></div>
    <div class="stat"><span class="v">${total}</span><span class="k">解答回数</span></div>
    <div class="stat"><span class="v">${acc}%</span><span class="k">正答率</span></div>`;

  // 科目別正答率(現モード)
  const pool = currentPool();
  const bySub = {};
  pool.forEach((q) => {
    const r = prog[q.id]; if (!r) return;
    const s = q.subject || 'その他';
    bySub[s] = bySub[s] || { c: 0, t: 0 };
    bySub[s].c += r.correct; bySub[s].t += r.correct + r.wrong;
  });
  const rows = Object.entries(bySub).map(([s, v]) => {
    const p = v.t ? Math.round((v.c / v.t) * 100) : 0;
    return `<div class="subj-row"><div>${s}<div class="bar"><span style="width:${p}%"></span></div></div><div>${p}% (${v.c}/${v.t})</div></div>`;
  }).join('');
  $('#statsBox').insertAdjacentHTML('beforeend',
    rows ? `<div class="subj-rows" style="grid-column:1/-1">${rows}</div>` : '');
}

/* ---------- 画面遷移 ---------- */
function show(screen) {
  ['home', 'quiz', 'result'].forEach((s) => { $('#' + s).hidden = s !== screen; });
  $('#homeBtn').hidden = screen === 'home';
  window.scrollTo(0, 0);
}

function goHome() {
  show('home');
  buildFilters();
  updatePoolInfo();
  renderStats();
  updateReviewCard();
  renderLog();
  syncStudyLog(todayStr()); // 演習で増えた今日のans等を同期
}

/* ---------- 演習 ---------- */
function startQuiz() {
  state.queue = buildQueue();
  if (!state.queue.length) { alert('この条件に該当する問題がありません。'); return; }
  state.idx = 0;
  state.review = false;
  state.session = { correct: 0, wrong: 0, results: [] };
  show('quiz');
  renderQuestion();
}

function renderQuestion() {
  const q = state.queue[state.idx];
  state.answered = false;
  $('#qProgress').textContent = `${state.idx + 1} / ${state.queue.length}`;
  $('#qBadge').textContent = q.__ol
    ? `${q.subject}${q.difficulty ? '・難易度' + q.difficulty : ''}`
    : `${q.yearLabel} 問${q.qnum}・${q.subject}`;
  $('#qText').textContent = q.question;
  $('#qFeedback').hidden = true;
  $('#qFeedback').className = 'feedback';
  $('#nextBtn').hidden = true;
  $('#nextBtn').textContent = state.idx + 1 < state.queue.length ? '次へ ›' : '結果を見る';

  const box = $('#qChoices');
  box.innerHTML = '';
  box.className = 'choices';

  if (q.__ol) return renderOX(q, box);
  if (q.type === 'choice') return renderChoice(q, box);
  if (q.type === 'multi') return renderMulti(q, box);
  return renderEssay(q, box);
}

/* ○× 一問一答 */
function renderOX(q, box) {
  box.classList.add('ox');
  [['○', '○'], ['×', '×']].forEach(([label, val]) => {
    const b = document.createElement('button');
    b.className = 'choice';
    b.textContent = label;
    b.onclick = () => gradeOX(q, val, box);
    box.appendChild(b);
  });
}
function gradeOX(q, val, box) {
  if (state.answered) return;
  const ok = val === q.answer;
  [...box.children].forEach((b) => {
    b.disabled = true;
    if (b.textContent === q.answer) b.classList.add('correct');
    else if (b.textContent === val) b.classList.add('wrong');
  });
  finish(q, ok, `正解: ${q.answer}`, q.explanation || '');
}

/* 5択 */
function renderChoice(q, box) {
  q.choices.forEach((ch) => {
    const b = document.createElement('button');
    b.className = 'choice';
    b.innerHTML = `<span class="num">${ch.key}</span><span>${escapeHtml(ch.text)}</span>`;
    b.onclick = () => gradeChoice(q, ch.key, box);
    box.appendChild(b);
  });
}
function gradeChoice(q, key, box) {
  if (state.answered) return;
  const allCorrect = q.answer === 'all';
  const ok = allCorrect || key === q.answer;
  [...box.children].forEach((b, i) => {
    b.disabled = true;
    const k = q.choices[i].key;
    if (!allCorrect && k === q.answer) b.classList.add('correct');
    if (k === key && !ok) b.classList.add('wrong');
    if (allCorrect) b.classList.add('correct');
  });
  const ans = allCorrect ? '全員正解(没問)' : `正解: ${q.answer}`;
  finish(q, ok, ans, q.note || '');
}

/* 多肢選択 (ア〜エを1〜20から) */
function renderMulti(q, box) {
  if (q.choices.length) {
    const bank = q.choices.map((c) => `${c.key}. ${c.text}`).join('　');
    box.insertAdjacentHTML('beforeend', `<div class="bank">${escapeHtml(bank)}</div>`);
  }
  const keys = ['ア', 'イ', 'ウ', 'エ'];
  const grid = document.createElement('div');
  grid.className = 'multi-grid';
  keys.forEach((k) => {
    const opts = q.choices.length
      ? q.choices.map((c) => `<option value="${c.key}">${c.key}. ${escapeHtml(c.text)}</option>`).join('')
      : Array.from({ length: 20 }, (_, i) => `<option value="${i + 1}">${i + 1}</option>`).join('');
    grid.insertAdjacentHTML('beforeend',
      `<label style="border:none;padding:0">${k}</label>
       <select data-k="${k}"><option value="">—</option>${opts}</select>`);
  });
  box.appendChild(grid);
  const btn = document.createElement('button');
  btn.className = 'primary'; btn.textContent = '採点する';
  btn.onclick = () => gradeMulti(q, grid);
  box.appendChild(btn);
}
function gradeMulti(q, grid) {
  if (state.answered) return;
  const ans = q.answer || {};
  let ok = true; const lines = [];
  grid.querySelectorAll('select').forEach((sel) => {
    const k = sel.dataset.k;
    const got = sel.value ? parseInt(sel.value, 10) : null;
    const right = ans[k];
    const good = got === right;
    if (!good) ok = false;
    lines.push(`${k}: あなた=${got ?? '未選択'} / 正解=${right}${good ? ' ✓' : ' ✗'}`);
  });
  finish(q, ok, '空欄の正解', lines.join('\n'));
}

/* 記述式(自己採点) */
function renderEssay(q, box) {
  box.insertAdjacentHTML('beforeend',
    `<div class="bank">記述式問題です。自動採点はできません。解答を考えてから自己採点してください。
（公式の正解例は別紙のため本アプリには収録していません）</div>`);
  const sg = document.createElement('div');
  sg.className = 'selfgrade';
  const mk = (label, ok) => {
    const b = document.createElement('button');
    b.textContent = label;
    b.onclick = () => { if (!state.answered) finish(q, ok, '自己採点', ''); };
    return b;
  };
  sg.appendChild(mk('できた', true));
  sg.appendChild(mk('できなかった', false));
  box.appendChild(sg);
}

/* 採点共通 */
function finish(q, ok, verdict, detail) {
  state.answered = true;
  const prev = loadProgress()[q.id];
  const base = (prev && prev.interval) || 0;
  recordResult(q.id, ok);
  applySrs(q.id, ok ? 'good' : 'again', base);
  bumpAnswered();
  if (ok) state.session.correct++; else state.session.wrong++;
  state.session.results.push({ q, ok });
  const cur = loadProgress()[q.id]; // applySrs 適用後の最新（due を表示に使う）
  const fb = $('#qFeedback');
  fb.hidden = false;
  fb.className = 'feedback ' + (ok ? 'ok' : 'ng');
  fb.innerHTML = `<div class="verdict">${ok ? '正解 ◎' : '不正解 ✗'}</div>
    <div class="exp"><b>${escapeHtml(verdict)}</b>${detail ? '\n' + escapeHtml(detail) : ''}</div>
    <div class="srs">📆 次の復習: <span id="srsDue">${srsLabel(cur.due)}</span>${ok ? ' <button id="hardBtn" class="hard-btn">△ あいまいだった</button>' : ''}</div>`;
  if (ok) {
    const hb = document.getElementById('hardBtn');
    if (hb) hb.onclick = () => {
      applySrs(q.id, 'hard', base);
      $('#srsDue').textContent = srsLabel(loadProgress()[q.id].due);
      hb.disabled = true;
    };
  }
  $('#nextBtn').hidden = false;
  $('#nextBtn').focus();
}

function next() {
  if (state.idx + 1 < state.queue.length) { state.idx++; renderQuestion(); }
  else renderResult();
}

/* ---------- 結果 ---------- */
function renderResult() {
  show('result');
  const { correct, wrong, results } = state.session;
  const total = correct + wrong;
  const acc = total ? Math.round((correct / total) * 100) : 0;
  $('#resScore').innerHTML =
    `<div class="big">${acc}%</div><div class="muted">${correct} / ${total} 問正解</div>`;
  const wrongs = results.filter((r) => !r.ok);
  $('#resList').innerHTML = results.map((r) =>
    `<div class="resitem ${r.ok ? '' : 'wrong'}">${r.ok ? '◎' : '✗'} ${badge(r.q)} ${escapeHtml(r.q.question.slice(0, 60))}…</div>`
  ).join('');
  $('#reviewWrongBtn').hidden = wrongs.length === 0;
  $('#reviewWrongBtn').onclick = () => {
    state.queue = wrongs.map((r) => r.q);
    state.idx = 0;
    state.session = { correct: 0, wrong: 0, results: [] };
    show('quiz'); renderQuestion();
  };
}
function badge(q) {
  return q.__ol ? `[${q.subject}]` : `[${q.yearLabel}問${q.qnum}]`;
}

/* ---------- utils ---------- */
function escapeHtml(s) {
  return String(s).replace(/[&<>"]/g, (c) =>
    ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
}

/* ---------- Firebase 認証・同期 ---------- */
function showLogin() {
  document.getElementById('loginApp').hidden = false;
  document.getElementById('app').hidden = true;
  $('#logoutBtn').hidden = true;
}

function hideLogin() {
  document.getElementById('loginApp').hidden = true;
  document.getElementById('app').hidden = false;
  $('#logoutBtn').hidden = false;
}

async function syncFromFirestore(uid) {
  try {
    const doc = await fbDb.collection('progress').doc(uid).get();
    if (!doc.exists) return;
    const remote = doc.data();
    const p = loadProgress();
    Object.assign(p, remote);
    saveProgress(p);
  } catch (e) { /* オフライン時はスキップ */ }
}

async function syncResult(id) {
  const user = fbAuth.currentUser;
  if (!user) return;
  const p = loadProgress();
  const r = p[id];
  if (!r) return;
  try {
    await fbDb.collection('progress').doc(user.uid).set(
      { [id]: r },
      { merge: true }
    );
  } catch (e) { /* オフライン時はスキップ */ }
}

async function syncStudyLog(date) {
  const user = fbAuth.currentUser;
  if (!user) return;
  const log = loadStudyLog();
  const e = log[date];
  if (!e) return;
  try {
    await fbDb.collection('studylog').doc(user.uid).set(
      { [date]: e },
      { merge: true }
    );
  } catch (err) { /* オフライン時はスキップ */ }
}

function showLoading() {
  const el = document.getElementById('loadingOverlay'); if (el) el.hidden = false;
  const h = document.getElementById('home'); if (h) h.hidden = true;
}
function hideLoading() {
  const el = document.getElementById('loadingOverlay'); if (el) el.hidden = true;
  const h = document.getElementById('home'); if (h) h.hidden = false;
}

async function syncStudyLogFromFirestore(uid) {
  try {
    const doc = await fbDb.collection('studylog').doc(uid).get();
    if (!doc.exists) return;
    const log = loadStudyLog();
    Object.assign(log, doc.data());
    saveStudyLog(log);
  } catch (e) { /* オフライン時はスキップ */ }
}

/* ---------- 初期化 ---------- */
async function init() {
  await loadData();
  $('#cntOne').textContent = state.oneliner.length;
  $('#cntExam').textContent = state.exam.length;

  document.querySelectorAll('.mode-card').forEach((b) =>
    b.addEventListener('click', () => setMode(b.dataset.mode)));
  ['#fSubject', '#fYear', '#fScope', '#fOrder', '#fCount'].forEach((s) =>
    $(s).addEventListener('change', updatePoolInfo));
  $('#startBtn').addEventListener('click', startQuiz);
  $('#reviewCard').addEventListener('click', startReview);
  $('#nextBtn').addEventListener('click', next);
  $('#homeBtn').addEventListener('click', goHome);
  $('#backHomeBtn').addEventListener('click', goHome);
  $('#resetBtn').addEventListener('click', () => {
    if (confirm('成績(正誤・正答率)をすべて削除します。よろしいですか?')) {
      localStorage.removeItem(PROGRESS_KEY); renderStats(); updateReviewCard();
    }
  });
  // 学習時間の加算ボタン(+15/+30/+60/−15)
  document.querySelectorAll('.log-btns button').forEach((b) =>
    b.addEventListener('click', () => addStudyMinutes(parseInt(b.dataset.min, 10))));

  setMode('oneliner');
  renderStats();
  updateReviewCard();
  renderLog();

  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('sw.js').catch(() => {});
  }
}

async function checkAuth() {
  // メールリンク踏んで戻ってきたとき
  if (fbAuth.isSignInWithEmailLink(location.href)) {
    let email = localStorage.getItem(EMAIL_KEY);
    if (!email) {
      email = prompt('確認のためメールアドレスを入力してください');
    }
    try {
      await fbAuth.signInWithEmailLink(email, location.href);
      localStorage.removeItem(EMAIL_KEY);
      history.replaceState(null, '', location.pathname); // URLからトークン除去
    } catch (e) {
      alert('ログインリンクが無効または期限切れです。再度メールを送信してください。');
      showLogin();
      return;
    }
  }

  // ログインボタン
  $('#sendMagicBtn').addEventListener('click', async () => {
    const email = $('#emailInput').value.trim();
    if (!email) return;
    $('#sendMagicBtn').disabled = true;
    $('#loginMsg').textContent = '送信中…';
    try {
      await fbAuth.sendSignInLinkToEmail(email, {
        url: location.origin + location.pathname,
        handleCodeInApp: true,
      });
      localStorage.setItem(EMAIL_KEY, email);
      $('#loginMsg').textContent = `${email} にログインリンクを送りました。メールのリンクをタップしてください。`;
    } catch (e) {
      $('#loginMsg').textContent = 'エラー: ' + (e.message || e);
      $('#sendMagicBtn').disabled = false;
    }
  });

  // ログアウトボタン
  $('#logoutBtn').addEventListener('click', async () => {
    await fbAuth.signOut();
  });

  // 認証状態を監視（セッション復元・ログアウト検知）
  let initialized = false;
  fbAuth.onAuthStateChanged(async (user) => {
    if (user) {
      hideLogin();
      const first = !initialized;
      if (first) showLoading();
      await syncFromFirestore(user.uid);
      await syncStudyLogFromFirestore(user.uid);
      if (first) {
        initialized = true;
        await init();
        hideLoading();
      } else {
        // 再認証（別端末からの同期反映）— 表示を更新
        renderLog(); renderStats(); updateReviewCard();
      }
    } else {
      showLogin();
    }
  });
}

checkAuth();
