# 行政書士 過去問演習アプリ — 構成書（AI読込用）

> このファイルは、別のAI／開発者がアプリ全体を短時間で把握するための仕様書。
> 最終更新: 2026-06-18 / SWキャッシュ版数: `gyosei-v5`

---

## 1. 概要

- **目的**: 行政書士試験の過去問演習PWA（個人学習用）。
- **形態**: 静的サイト（ビルド不要のvanilla JS）。サーバ側ロジックなし。
- **公開URL**: https://three100.github.io/gyosei-kakomon/
- **ホスティング**: GitHub Pages（公開リポジトリ `ThREE100/gyosei-kakomon`、`main`ブランチの`app/`を配信）。
- **更新方法**: `app/`で`git push`するとPagesが自動再ビルド。
- **対応**: PWA（オフライン動作・ホーム画面追加可・iPhone対応）。

---

## 2. 技術スタック

| 領域 | 採用技術 |
|------|----------|
| フロント | 素のHTML / CSS / JavaScript（フレームワーク・ビルド無し） |
| 状態保存 | localStorage（成績・学習記録・認証用メール） |
| 認証 | Firebase Authentication（メールリンク／マジックリンク方式） |
| クラウド同期 | Cloud Firestore（成績・学習記録を端末間同期） |
| オフライン | Service Worker（`sw.js`、cache-first） |
| データ生成 | Python 3 + PyMuPDF（公式PDF/HTMLからJSON生成） |

外部CDN: Firebase compat SDK v10.12.2（app / auth / firestore の3本、`index.html`で読込）。

---

## 3. ファイル構成

```
行政書士試験_アプリ開発/
├── app/                      ← 配信される本体（これがGitHub Pagesのルート）
│   ├── index.html            UI骨格（ログイン画面＋ホーム＋演習＋結果）
│   ├── app.js                全ロジック（~25KB, vanilla JS, 'use strict'）
│   ├── style.css             スタイル（ダーク/ライト自動切替）
│   ├── sw.js                 Service Worker（CACHE='gyosei-v5'）
│   ├── manifest.json         PWAマニフェスト
│   ├── icon-180/192/512.png  アイコン
│   └── data/
│       ├── exam.json         本試験形式 332問（641KB）
│       └── oneliner.json     一問一答（肢別）2163問（1.7MB）
├── scripts/                  データ生成3本（再生成時のみ使用）
│   ├── parse_answers.py      公式の正解HTML(rXans.html)を解析
│   ├── parse_questions.py    公式の問題PDF(rX_mondai.pdf)を解析
│   └── build_dataset.py      正解と問題を結合 → exam.json生成
├── data/raw/                 公式DL元（令和2〜7年度のPDF/HTML）
├── firestore.rules           Firestoreセキュリティルール
├── questions.json            一問一答の元データ（→ oneliner.jsonの素材）
└── README.md
```

---

## 4. 収録問題数とその内訳

### 総数
- **本試験形式（exam.json）: 332問**
- **一問一答／肢別（oneliner.json）: 2163問**
- 合計 **2495問**

### 4-1. 本試験形式 exam.json（332問）

出題形式別:
| type | 件数 | 説明 |
|------|------|------|
| `choice` | 296 | 5択（択一式）。自動採点。 |
| `multi`  | 18 | 多肢選択（ア〜エの空欄に語句バンク1〜20から選択）。自動採点。 |
| `essay`  | 18 | 記述式（40字程度）。**自動採点不可・自己採点**。公式正解例は別紙のため非収録。 |

年度別（令和2〜7年度の6年分）:
| 年度 | 件数 |
|------|------|
| 令和2年度 | 55 |
| 令和3年度 | 55 |
| 令和4年度 | 56 |
| 令和5年度 | 54 |
| 令和6年度 | 56 |
| 令和7年度 | 56 |

科目別:
| 科目 | 件数 |
|------|------|
| 行政法 | 132 |
| 民法 | 66 |
| 一般知識等 | 65 |
| 憲法 | 33 |
| 商法・会社法 | 30 |
| 基礎法学 | 6 |

> 注: 公式の本試験は各年60問だが、著作権配慮で非掲載の問題（問1・58〜60等）を除外しているため年あたり54〜56問。

### 4-2. 一問一答／肢別 oneliner.json（2163問）

すべて○×形式。正解分布: ×=1191 / ○=972。

科目別:
| 科目 | 件数 |
|------|------|
| 行政法 | 843 |
| 民法 | 651 |
| 憲法 | 347 |
| 商法・会社法 | 172 |
| 業務関連諸法令 | 77 |
| 情報通信・個人情報保護 | 43 |
| 基礎法学 | 30 |

---

## 5. データスキーマ

### oneliner.json（要素＝1肢）
```jsonc
{
  "id": 1,                       // 数値ID（アプリ内では "OL-..." ではなく元のidを使用）
  "subject": "憲法",             // 科目（絞り込みキー）
  "section": "1 最高法規",       // 章
  "subsection": "",              // 節
  "difficulty": "B",             // 難易度 A/B/C（バッジ表示に使用）
  "year_codes": ["H17-3-5", ...],// 出典の本試験番号（表示には未使用）
  "question": "国民、天皇又は...", // 問題文
  "answer": "○" | "×",           // 正解
  "explanation": "...憲法99条..."  // 解説
}
```
※ アプリ読込時に全要素へ `__ol: true` を付与。`id`が無い場合は `OL-{連番}` を補完。

### exam.json（要素＝1問）
共通フィールド: `id`（例 "R2-2"）, `seq`（通し番号）, `year`（"R2"）, `yearLabel`（"令和2年度"）, `qnum`（問番号）, `type`, `subject`, `question`。

- **type=choice**:
```jsonc
{
  "type": "choice",
  "choices": [{ "key": 1, "text": "ア・イ" }, ...],  // 5択
  "answer": 4,            // 正解キー（"all"なら全員正解＝没問扱い）
  "note": ""              // 補足（あれば解説相当）
}
```
- **type=multi**:
```jsonc
{
  "type": "multi",
  "choices": [{ "key": 1, "text": "統制" }, ... 20件],  // 語句バンク
  "answer": { "ア": 20, "イ": 8, "ウ": 17, "エ": 1 }    // 空欄ごとの正解キー
}
```
- **type=essay**:
```jsonc
{ "type": "essay", "choices": [], "answer": null }      // 自己採点（自動採点なし）
```
※ アプリ読込時に全要素へ `__ol: false` を付与。

---

## 6. 機能

### 出題
- 2モード: **一問一答（○×）** / **本試験形式（5択・多肢・記述）**。
- 絞り込み: 科目・年度（本試験のみ）・範囲（すべて/未挑戦のみ/間違えた問題）・出題順（順番/シャッフル）・問題数（10/20/50/全）。
- 採点後フィードバック（正誤・正解・解説）と「次へ」。結果画面で正答率・誤答リスト・「間違えた問題を復習」。

### 間隔反復（忘却曲線・SM-2簡易版）
- 各問の記録に `interval`（日数）と `due`（次回出題日 YYYY-MM-DD）を保持。
- 採点で間隔更新: **×→1日 / △(あいまい)→base×1.3 / ○→base×2.5**（新規は1日）。
- ホームに「**今日の復習 N問**」カード（`due <= 今日`の問題数）。一問一答＋本試験の**混在キュー**で出題。
- 1セッション上限 **`REVIEW_CAP=20`問**（溜まり過ぎても一度に出し過ぎない）。
- 正解時のみ「△あいまいだった」ボタンで間隔を短く再設定可能。

### 学習記録（時間・継続トラッカー）
- localStorage `gyosei_studylog_v1` = `{ "YYYY-MM-DD": { min, ans } }`。
  - `min` = 手動入力（+15/+30/+60/−15分ボタン、0未満クランプ）。
  - `ans` = 採点時に自動+1（`bumpAnswered()`）。
- 表示: 今日の時間/目標バー（**平日180分・土日150分**）、🔥連続学習日（`min>0`または`ans>0`で学習日判定。今日未着手でも前日までの連続は維持）、今週/20h、累計/408h、現在フェーズ、直近5週ヒートマップ（曜日ラベル付き、`min>0`または`ans>0`で色付け、濃淡4段階）。
- 学習計画の5フェーズ（`PHASES`定数）と日付で連動表示。

### 学習計画（前提）
- 試験日 **2026/11/8**。学習ペース 平日3h×5＋土日各2.5h ＝ **週20h・総計約408h**。
- 5フェーズ: ①インプット126h（〜7/31）/②アウトプット88h（8月）/③演習＋記述86h（9月）/④仕上げ88h（10月）/⑤直前22h（11/1〜8）。

---

## 7. 認証・クラウド同期

- **Firebase Authentication**: メールリンク（マジックリンク）方式。パスワード不要。
  - `firebaseConfig`は`app.js`先頭に直書き（公開前提のクライアントキー、`projectId=gyosei-kakomon`）。
  - 認証ドメインに `three100.github.io` 登録済み。
- **Firestore 同期**（オフライン時はスキップ・端末間マージ方式）:
  | コレクション | ドキュメント | 内容 |
  |--------------|--------------|------|
  | `progress`   | `{uid}` | 全問の成績（フィールド＝問題ID → `{correct, wrong, last, interval, due}`）。`merge:true`でupsert。 |
  | `studylog`   | `{uid}` | 学習記録（フィールド＝日付 → `{min, ans}`）。`merge:true`でupsert。 |
- **セキュリティルール**（`firestore.rules`）: `progress/{userId}`・`studylog/{userId}` ともに `request.auth.uid == userId` のときのみ read/write 許可。

---

## 8. localStorage キー一覧

| キー | 内容 |
|------|------|
| `gyosei_progress_v1` | 成績（問題ID → `{correct, wrong, last, interval, due}`） |
| `gyosei_studylog_v1` | 学習記録（日付 → `{min, ans}`） |
| `gyosei_email_for_signin` | マジックリンク送信時のメール（ログイン完了で削除） |

---

## 9. データの再生成（年度追加時）

1. `data/raw/` に公式の新年度PDF（`rX_mondai.pdf`）と正解HTML（`rXans.html`）をDL。
2. `scripts/` の3本を順に実行（要 `pip install pymupdf`）:
   `parse_answers.py` → `parse_questions.py` → `build_dataset.py`。
3. 出力された `exam.json` を `app/data/` に配置 → `git push`。

> データ方針: 収集元は**公式サイト（行政書士試験研究センター gyosei-shiken.or.jp）のみ**。商用サイトはスクレイピングしない。著作権非掲載問題は除外。記述式の公式正解例は別紙のため非収録（自己採点）。「全員正解」は `answer:"all"`。

---

## 10. 主要関数マップ（app.js）

| 領域 | 関数 |
|------|------|
| 進捗 | `loadProgress` `saveProgress` `recordResult` |
| 間隔反復 | `applySrs` `dueQuestions` `srsLabel` `updateReviewCard` `startReview`（`REVIEW_CAP=20`） |
| 学習記録 | `loadStudyLog` `addStudyMinutes` `bumpAnswered` `studyStreak` `weekMinutes` `totalMinutes` `currentPhase` `calendarCells` `renderLog` |
| 出題 | `loadData` `buildQueue` `startQuiz` `renderQuestion` `renderOX/Choice/Multi/Essay` `finish` `renderResult` |
| 認証・同期 | `checkAuth` `syncFromFirestore` `syncResult` `syncStudyLog` `syncStudyLogFromFirestore` `showLoading/hideLoading` |
| 初期化 | `init`（`onAuthStateChanged`内で初回のみ実行） |
