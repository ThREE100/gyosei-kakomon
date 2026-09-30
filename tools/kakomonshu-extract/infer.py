"""欠損の推定(信頼度B)。restore.py の後に実行する。

  python infer.py prepare   # 未補完(C)の肢ごとの入力を work/infer/inputs/ に出力
  (PowerShell) .\\run-infer.ps1   # claude -p で各肢の補完案を work/infer/outputs/ に出力
  python infer.py apply     # 補完案を検査して out/book.restored.json に反映、確認用一覧 out/infer-review.md を出力

検査: 結論を逆転させる語(数字・否定・のみ/限り/以上 等)に関わる補完は自動で却下し、〓のまま残す(C)。
推定Bはすべて review_required=true で、人が確認するまで図解の本文には使わない。
"""
import json, os, re, sys, unicodedata

ROOT = os.path.dirname(os.path.abspath(__file__))
IN = os.path.join(ROOT, "work", "infer", "inputs")
OUT = os.path.join(ROOT, "work", "infer", "outputs")
BOOK = os.path.join(ROOT, "out", "book.restored.json")

NUM = r"[0-9０-９一二三四五六七八九十百千万]"
CRIT = re.compile(
    NUM + r"|ない|なく|なかっ|ず|ぬ|不|非|無|未|のみ|限り|限る|限ら|だけ|以上|以下|以内|超|満|すべて|全て|全部|必ず|常に|決して|"
    r"原則|例外|いずれ|かつ|または|又は|及び|並びに|若しくは|もしくは|のに|ものの|のでは|ではな")

def strip_tags(s): return re.sub(r"</?[ub]>", "", s or "")

def find_marks(text):
    return [m.start() for m in re.finditer("〓", text)]

def critical(text, idx, fill):
    """idx番目の〓を fill で置換したとき、fillの位置に重なる形で結論逆転語が現れるか。"""
    t = strip_tags(text)
    marks = find_marks(t)
    if idx < 1 or idx > len(marks): return "indexが不正"
    pos = marks[idx - 1]
    # 他の〓は仮の '□' に置き、fillの前後3字を含めて判定
    t2 = t[:pos].replace("〓", "□") + fill + t[pos + 1:].replace("〓", "□")
    lo, hi = max(0, pos - 3), pos + len(fill) + 3
    window = t2[lo:hi]
    a, b = pos - lo, pos - lo + len(fill)
    for m in CRIT.finditer(window):
        if m.start() < b and m.end() > a:
            return f"結論を左右しうる語に関与: 「{m.group(0)}」"
    return None

def prepare():
    book = json.load(open(BOOK, encoding="utf-8"))
    os.makedirs(IN, exist_ok=True); n = 0
    for it in book["items"]:
        if (it.get("restore") or {}).get("tier") != "C": continue
        d = {"seq": it["seq"], "heading_path": it.get("heading_path"), "answer": it.get("answer"),
             "question_text": it.get("question_text"), "explanation_text": it.get("explanation_text")}
        json.dump(d, open(os.path.join(IN, f"{it['seq']:05d}.json"), "w", encoding="utf-8"), ensure_ascii=False)
        n += 1
    print(f"prepared {n} items -> {IN}")

def apply():
    book = json.load(open(BOOK, encoding="utf-8"))
    rev, rej = [], []
    nb = 0
    for it in book["items"]:
        if (it.get("restore") or {}).get("tier") != "C": continue
        p = os.path.join(OUT, f"{it['seq']:05d}.json")
        if not os.path.exists(p): continue
        try: o = json.load(open(p, encoding="utf-8"))
        except Exception: rej.append(f"- #{it['seq']}: 出力JSONが不正"); continue
        text = it["question_text"]; marks = find_marks(strip_tags(text)); n = len(marks)
        accepted, rejected = {}, []
        for f in o.get("fills", []):
            i, t = f.get("index"), (f.get("text") or "")
            if not isinstance(i, int) or not (1 <= i <= n) or not (1 <= len(t) <= 8): rejected.append((i, t, "形式不正")); continue
            why = critical(text, i, t)
            if why: rejected.append((i, t, why)); continue
            accepted[i] = f
        for i in o.get("cannot_infer", []): rejected.append((i, "", "推定不能(モデル判断)"))
        if accepted:
            # 採用した〓だけ置換(タグ付き本文の〓を出現順に)
            cnt = 0
            def sub(m):
                nonlocal cnt
                cnt += 1
                return accepted[cnt]["text"] if cnt in accepted else "〓"
            inferred = re.sub("〓", sub, text)
            it["question_inferred"] = inferred
            it["restore"] = {"tier": "B", "source": "inferred", "review_required": True,
                             "fills": [{"index": i, **accepted[i]} for i in sorted(accepted)],
                             "remaining_gaps": n - len(accepted)}
            nb += 1
            rev.append(f"### #{it['seq']} p{it.get('pdf_page_q')} 肢{it.get('stmt_no')} {'/'.join(it.get('heading_path') or [])} (答: {it.get('answer')})\n"
                       f"- 原文: {text}\n- 推定: {inferred}\n" +
                       "\n".join(f"  - 〓{i}→「{accepted[i]['text']}」 [{accepted[i].get('confidence')}] {accepted[i].get('basis')}" for i in sorted(accepted)) +
                       (f"\n- 未補完の〓: {n-len(accepted)}か所" if n - len(accepted) else ""))
        for i, t, why in rejected:
            rej.append(f"- #{it['seq']} p{it.get('pdf_page_q')} 〓{i} {('「'+t+'」') if t else ''}: {why}")
    json.dump(book, open(BOOK, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    rep = ["# 推定(B)の確認用一覧", "", f"- 推定を含む肢: {nb}件(すべて要確認。確認前は図解の本文に使わない)", "", "## 推定案", ""] + rev + ["", "## 却下・推定不能(〓のまま残る)", ""] + rej
    open(os.path.join(ROOT, "out", "infer-review.md"), "w", encoding="utf-8").write("\n".join(rep))
    print(f"B: {nb}件 / 却下・推定不能: {len(rej)}件 -> out/infer-review.md")

if __name__ == "__main__":
    {"prepare": prepare, "apply": apply}.get(sys.argv[1] if len(sys.argv) > 1 else "", lambda: sys.exit(__doc__))()
