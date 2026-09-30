"""work/chunks/*.json を、見出し階層を付与しながら1つの構造化JSON(out/book.json)に統合する。

- 見出し(heading)は読み順に追跡し、後続の肢に heading_path(科目>章>節>項)を付ける
- 重なりページ(Overlap)で重複した肢は、より完全なもの(confidence・欠損の少なさ)を残す
- 他チャンクにまたがる問題側/解説側は、同じ (pdf_page_q, stmt_no, rank) のもの同士で補完する
"""
import json, glob, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
CONF = {"high": 3, "medium": 2, "low": 1}

def score(it):
    filled = sum(1 for k in ("question_text", "answer", "explanation_text") if it.get(k))
    return (filled, CONF.get(it.get("confidence"), 0), len(it.get("uncertain") or []) * -1)

def key(it):
    q = re.sub(r"\s+", "", it.get("question_text") or "")[:20]
    return (it.get("pdf_page_q"), it.get("stmt_no"), it.get("rank"), q)

def main():
    files = sorted(glob.glob(os.path.join(ROOT, "work", "chunks", "*.json")))
    if not files:
        sys.exit("work/chunks に入力がありません")
    path = {}          # level -> text
    items, others, headings = {}, [], []
    order = []
    for f in files:
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception as e:
            print("WARN parse", f, e); continue
        for b in d.get("blocks", []):
            t = b.get("type")
            if t == "heading":
                lv = int(b.get("level") or 1)
                path = {k: v for k, v in path.items() if k < lv}
                path[lv] = b.get("text", "")
                headings.append({"level": lv, "text": b.get("text", ""), "pdf_page": b.get("pdf_page"),
                                 "path": [path[k] for k in sorted(path)]})
            elif t == "item":
                b = dict(b)
                b["heading_path"] = [path[k] for k in sorted(path)]
                b["source_chunk"] = os.path.basename(f)
                k = key(b)
                # 見出しが未確定(最初のチャンク以外で重複)の場合は、既存側の見出しを優先
                if k in items:
                    old = items[k]
                    if score(b) > score(old):
                        if not b["heading_path"]: b["heading_path"] = old["heading_path"]
                        items[k] = b
                else:
                    items[k] = b; order.append(k)
            elif t == "other":
                # 重複除去(重なりページ)
                sig = (b.get("kind"), b.get("pdf_page"), (b.get("text") or "")[:30])
                if sig not in {(o.get("kind"), o.get("pdf_page"), (o.get("text") or "")[:30]) for o in others}:
                    others.append(b)
    out = [items[k] for k in order]
    out.sort(key=lambda x: (x.get("pdf_page_q") or 0, x.get("stmt_no") or 0))
    for i, it in enumerate(out, 1):
        it["seq"] = i
    os.makedirs(os.path.join(ROOT, "out"), exist_ok=True)
    book = {"meta": {"chunks": len(files), "items": len(out)}, "headings": headings, "items": out, "other": others}
    p = os.path.join(ROOT, "out", "book.json")
    json.dump(book, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"merged {len(files)} chunks -> {p}: items={len(out)} headings={len(headings)} other={len(others)}")

if __name__ == "__main__":
    main()
