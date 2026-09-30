"""欠損位置(〓)を、独立した参照資料で補う(信頼度A)。補えなかったものは未補完(C)として残す。

入力: out/book.json(merge.py の出力)
出力: out/book.restored.json(各肢に restore 情報を追加) と out/restore-report.md

方針(厳守):
 - 原文(question_text)は書き換えず、question_restored に補完後の文を入れる。出所を restore に記録する。
 - 参照文に「見えている断片がすべて・順序どおり・近い間隔で」含まれる場合だけ採用する(1字でも食い違えば不採用)。
 - 各〓に対し、参照文側に1〜8字の欠けた部分が存在する場合だけ埋める(参照側も同じ位置で欠けていれば不採用)。
 - 信頼度: A=公式問題(data/exam.json)と一致 / A2=oneliner.json と一致(同じスキャン由来でOCR誤りもあり得るため要確認)
 - 推定(B)は別工程。ここでは行わない。
"""
import json, os, re, sys, unicodedata, collections

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(ROOT, "..", ".."))
MAXGAP = 8

def strip_tags(s): return re.sub(r"</?[ub]>", "", s or "")
def norm(s): return re.sub(r"\s+", "", unicodedata.normalize("NFKC", s or ""))

def load_candidates():
    """exam_ref('R3-8-2' など)→ [(出所, 文)] を作る。"""
    cand = collections.defaultdict(list)
    ex = json.load(open(os.path.join(REPO, "data", "exam.json"), encoding="utf-8"))
    for q in ex:
        if q.get("type") != "choice": continue
        qid = q["id"]                                   # 'R3-8'
        ch = q.get("choices")
        if isinstance(ch, str):
            try: ch = json.loads(ch.replace("'", '"'))
            except Exception: ch = None
        for c in ch or []:
            cand[f"{qid}-{c['key']}"].append(("A", f"exam.json:{qid}-{c['key']}", c["text"]))
        # ア〜オ形式(問題文中の「ア …」)
        m = re.findall(r"(?m)^([アイウエオ])\s*(.+?)(?=^[アイウエオ]\s|\Z)", q.get("question", ""), flags=re.S)
        for k, t in m:
            cand[f"{qid}-{k}"].append(("A", f"exam.json:{qid}-{k}", t))
    ol_path = os.path.join(REPO, "data", "oneliner.json")
    if os.path.exists(ol_path):
        for o in json.load(open(ol_path, encoding="utf-8")):
            for c in o.get("year_codes") or []:
                cand[c.replace("·", "・")].append(("A2", f"oneliner.json:id={o['id']}", o["question"]))
    return cand

def try_fill(text, ref):
    """text: 〓入りの本文(タグ付き)。ref: 参照文。成功すれば (補完後テキスト, [補った語]) を返す。"""
    frags = text.split("〓")
    r = norm(ref)
    pos, out, gaps = None, [], []
    for i, fr in enumerate(frags):
        f = norm(strip_tags(fr))
        if i == 0:
            if not f: continue
            p = r.find(f)
            if p < 0 or p > 3: return None
        else:
            lo = pos + 1
            if f:
                p = r.find(f, lo)
                if p < 0 or p - pos > MAXGAP: return None
            else:                       # 末尾の〓(以降に断片なし)
                p = len(r)
                if not (1 <= p - pos <= MAXGAP): return None
            gaps.append(r[pos:p])
        pos = p + len(f)
    if len(r) - pos > 3: return None     # 参照文に、未照合の長い残りがある
    # 補完後テキスト(タグは維持)を組み立てる
    res, gi = frags[0], 0
    for fr in frags[1:]:
        res += gaps[gi] + fr; gi += 1
    return res, gaps

def main():
    book = json.load(open(os.path.join(ROOT, "out", "book.json"), encoding="utf-8"))
    cand = load_candidates()
    stat = collections.Counter(); lines = []
    for it in book["items"]:
        q = it.get("question_text") or ""
        if "〓" not in q:
            continue
        done = None
        for ref in it.get("exam_refs") or []:
            for tier, src, txt in cand.get(ref.replace("·", "・"), []):
                r = try_fill(q, txt)
                if r and (done is None or tier < done["tier"]):
                    done = {"tier": tier, "source": src, "filled": r[1], "text": r[0]}
        if done:
            it["question_restored"] = done["text"]
            it["restore"] = {"tier": done["tier"], "source": done["source"], "filled": done["filled"],
                             "review_required": done["tier"] != "A"}
            stat[done["tier"]] += 1
        else:
            it["restore"] = {"tier": "C", "source": None, "filled": [], "review_required": True}
            stat["C"] += 1
            lines.append(f"- #{it['seq']} p{it.get('pdf_page_q')} 肢{it.get('stmt_no')} {'/'.join(it.get('heading_path') or [])} refs={it.get('exam_refs')}")
    p = os.path.join(ROOT, "out", "book.restored.json")
    json.dump(book, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    rep = ["# 補完レポート", "", f"- 欠損(〓)を含む肢: {sum(stat.values())}件",
           f"- A(公式問題で確定): {stat['A']}件 / A2(oneliner一致・要確認): {stat['A2']}件 / C(未補完): {stat['C']}件", "",
           "## 未補完(C)の一覧(推定Bの対象)", ""] + lines
    open(os.path.join(ROOT, "out", "restore-report.md"), "w", encoding="utf-8").write("\n".join(rep))
    print(dict(stat), "->", p)

if __name__ == "__main__":
    main()
