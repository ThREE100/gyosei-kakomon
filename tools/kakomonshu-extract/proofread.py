"""公式問題(gyosho_past_questions.json)で、読み取りデータの校正と欠損補完を行う。

  python proofread.py ocr   --official PATH --book PATH     # YomiToku OCRのページ別JSON(検証用)
  python proofread.py items --official PATH [--in out\\book.restored.json]   # Claude読み取り(merge/restore後)の肢

公式問題の選択肢(問題文の各行)と、本書の肢を文字単位で突き合わせ、差分を分類する:
  cut       : 行末で欠けた文字(右端欠け)。公式側にだけある1〜8字。→ 補完(信頼度A)
  cut+fix   : 欠けと誤読が同じ位置(例: 将来→特)。→ 補完
  ocr       : 1〜3字の誤読(例: 蹂躙→膝濁)。→ 校正案
  noise     : 余計な記号・ページ見出しの混入。→ 除去案
  modified  : 上記以外の差分が大きい=本書が書き換えた肢(改題)。→ 触らない
採用条件: 本文の一致率が0.85以上で、差分がすべて上記に分類できること。1つでも分類できない差分があれば触らない。
公式問題データは著作物の再配布にあたるためリポジトリに入れない(--official でローカルのパスを指定)。
"""
import argparse, collections, difflib, json, os, re, sys, unicodedata

ROOT = os.path.dirname(os.path.abspath(__file__))

def nz(s):
    s = unicodedata.normalize("NFKC", s).replace("·", "・").replace("･", "・")
    return re.sub(r"\s+", "", s)

def tri(s): return {s[i:i + 3] for i in range(len(s) - 2)}

class Official:
    def __init__(self, path):
        self.lines = []
        for q in json.load(open(path, encoding="utf-8")):
            for i, l in enumerate(x.strip() for x in q["question"].split("\n") if x.strip()):
                if len(l) >= 12:
                    self.lines.append({"title": q["page_title"], "text": l, "n": nz(l)})
        self.inv = collections.defaultdict(list)
        for ci, c in enumerate(self.lines):
            for t in tri(c["n"]): self.inv[t].append(ci)

    def best(self, n):
        cnt = collections.Counter()
        for t in tri(n):
            for ci in self.inv.get(t, ()): cnt[ci] += 1
        best = None
        for ci, _ in cnt.most_common(6):
            r = difflib.SequenceMatcher(None, n, self.lines[ci]["n"], autojunk=False).ratio()
            if not best or r > best[0]: best = (r, ci)
        return best

def classify(J, O, brk):
    """J(本書)をO(公式)に合わせる差分を分類。戻り値: (種別, 差分リスト)。"""
    sm = difflib.SequenceMatcher(None, J, O, autojunk=False)
    fixes, ok = [], True
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal": continue
        near = any(abs(i1 - k) <= 1 or abs(i2 - k) <= 1 for k in brk)
        if tag == "insert" and (j2 - j1) <= 8 and near: fixes.append(("cut", i1, i2, O[j1:j2]))
        elif tag == "insert" and (j2 - j1) <= 8 and i1 >= len(J) - 1: fixes.append(("cut", i1, i2, O[j1:j2]))
        elif tag == "replace" and (i2 - i1) <= 2 and (j2 - j1) <= 8 and near: fixes.append(("cut+fix", i1, i2, O[j1:j2]))
        elif tag == "replace" and (i2 - i1) <= 3 and (j2 - j1) <= 3: fixes.append(("ocr", i1, i2, O[j1:j2]))
        elif tag == "delete" and (i2 - i1) <= 2: fixes.append(("noise", i1, i2, ""))
        elif tag == "delete" and (i2 - i1) <= 12 and (i1 == 0 or i2 >= len(J) - 1): fixes.append(("noise", i1, i2, ""))
        else: ok = False
    return ok, fixes, sm.ratio()

def run_ocr(off, book_path, out_path):
    B = json.load(open(book_path, encoding="utf-8"))
    start = re.compile(r"^(\d{1,2})[ 　]+(\S.*)$")
    ref = re.compile(r"^\(?[SHR][ 元\d]*-\s*\d+-\s*\S+\)?$")
    stm = []
    for pg in B["pages"]:
        cur = None
        for ln in pg["text"].split("\n"):
            s = ln.strip(); m = start.match(s)
            if m and 1 <= int(m.group(1)) <= 20 and not re.match(r"^[xXOo×○]\s", m.group(2)):
                cur = {"page": pg["page"], "no": int(m.group(1)), "lines": [m.group(2)]}; stm.append(cur); continue
            if cur and (ref.match(s) or re.match(r"^[ABC]$", s)): cur = None
            elif cur and s and not re.match(r"^\d+\s*\S{0,6}$", s): cur["lines"].append(s)
    stm = [x for x in stm if sum(len(l) for l in x["lines"]) >= 15]
    cat = collections.Counter(); out = []
    for s in stm:
        pieces = [nz(l) for l in s["lines"]]; J = "".join(pieces); brk, acc = [], 0
        for p in pieces[:-1]: acc += len(p); brk.append(acc)
        b = off.best(J)
        if not b or b[0] < 0.6: cat["照合なし"] += 1; continue
        ok, fixes, r = classify(J, off.lines[b[1]]["n"], brk)
        kind = "一致" if not fixes and ok else ("校正・補完可" if ok and r >= 0.85 else "改題(触らない)")
        cat[kind] += 1
        if kind == "校正・補完可":
            for f in fixes: cat["  " + f[0]] += 1
            out.append({"page": s["page"], "no": s["no"], "official": off.lines[b[1]]["title"], "ratio": round(r, 3),
                        "fixes": [{"kind": f[0], "book": J[f[1]:f[2]], "official": f[3]} for f in fixes]})
    json.dump(out, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"statements={len(stm)}"); [print(f"{k}: {v}") for k, v in cat.items()]
    print("->", out_path)

def run_items(off, inp, outp):
    book = json.load(open(inp, encoding="utf-8"))
    n_fill = n_sug = 0; sug = []
    for it in book["items"]:
        q = it.get("question_text") or ""
        if not q or (it.get("restore") or {}).get("tier") in ("A", "A2") and "〓" not in q: continue
        plain = re.sub(r"</?[ub]>", "", q)
        # 〓を外した本文Jと、〓の位置(欠損位置)
        J, brk = "", []
        for ch in plain:
            if ch == "〓": brk.append(len(nz(J)))
            else: J += ch
        J = nz(J)
        b = off.best(J)
        if not b or b[0] < 0.6: continue
        ok, fixes, r = classify(J, off.lines[b[1]]["n"], brk)
        if not ok or r < 0.85: continue
        cuts = [f for f in fixes if f[0] in ("cut", "cut+fix")]
        if brk and cuts and len(cuts) >= len(brk) and "〓" in q:
            # 〓の数と補完位置が一致するときだけ、〓を順に置換(タグは維持)
            fills = [f[3] for f in sorted(cuts, key=lambda x: x[1])][:len(brk)]
            it_iter = iter(fills)
            it["question_restored"] = re.sub("〓", lambda m: next(it_iter), q)
            it["restore"] = {"tier": "A", "source": "gyosho:" + off.lines[b[1]]["title"], "filled": fills, "review_required": False}
            n_fill += 1
        for f in fixes:
            if f[0] in ("ocr", "noise"):
                sug.append({"seq": it.get("seq"), "kind": f[0], "book": J[f[1]:f[2]], "official": f[3], "official_title": off.lines[b[1]]["title"]})
    book["proofread_suggestions"] = sug
    json.dump(book, open(outp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"〓を補完(A): {n_fill}件 / 校正案(ocr・noise): {len(sug)}件 -> {outp}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("mode", choices=["ocr", "items"])
    ap.add_argument("--official", required=True); ap.add_argument("--book"); ap.add_argument("--in", dest="inp")
    a = ap.parse_args(); off = Official(a.official)
    os.makedirs(os.path.join(ROOT, "out"), exist_ok=True)
    if a.mode == "ocr":
        run_ocr(off, a.book, os.path.join(ROOT, "out", "proofread-ocr.json"))
    else:
        p = a.inp or os.path.join(ROOT, "out", "book.restored.json")
        run_items(off, p, p)
