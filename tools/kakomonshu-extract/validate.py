"""out/book.json を検証し、out/report.md に要確認リストを出す。

チェック:
 1. 必須項目・値の形式(rank, answer, exam_refs)
 2. 文字種(簡体字・ハングル・キリル・置換文字�、読めない文字〓、疑似文字)
 3. 肢番号の連続性(同じ見出し配下で 1,2,3… に欠番がないか)
 4. 既存 data/oneliner.json との照合(出題履歴が重なる肢で、本文が「ほぼ一致だが数文字違う」ものを誤認識候補として列挙)
 5. confidence が low/medium、uncertain のある肢
"""
import json, os, re, sys, unicodedata, difflib, collections

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(ROOT, "..", ".."))

# 日本語では使わない簡体字(代表例)。過去のOCRで混入した脑・发・权・记 などを含む
SIMPLIFIED = set("们这说为时问关对发权记见现动进还经济产条约员议实达运开专书车东两个门题间应总组织决际级脑执营团报边达张让计设该证诉认识讲许论调谈")
# ↑「条」「団」など日本語と字体が同じものが混ざらないよう下で除外
SIMPLIFIED -= set("条")
REF_RE = re.compile(r"^(H|R|S)(元|\d{1,2})-\d{1,2}-[^\s]{1,8}$")

def script_flags(text):
    fl = set()
    for ch in text or "":
        if ch in SIMPLIFIED: fl.add(f"簡体字?:{ch}")
        if ch == "�": fl.add("置換文字")
        if ch == "〓": fl.add("判読不能〓")
        try: n = unicodedata.name(ch)
        except ValueError: fl.add(f"不明文字:U+{ord(ch):04X}"); continue
        if n.startswith("HANGUL"): fl.add("ハングル")
        if n.startswith("CYRILLIC"): fl.add("キリル")
    return fl

def norm(s):
    s = unicodedata.normalize("NFKC", s or "")
    s = re.sub(r"</?[ub]>", "", s)
    return re.sub(r"[\s、。,.・·「」『』()（）]", "", s)

def main():
    book = json.load(open(os.path.join(ROOT, "out", "book.json"), encoding="utf-8"))
    items = book["items"]
    rep = collections.defaultdict(list)

    for it in items:
        tag = f"#{it['seq']} p{it.get('pdf_page_q')} 肢{it.get('stmt_no')} {'/'.join(it.get('heading_path') or [])}"
        if it.get("rank") not in ("A", "B", "C"): rep["rank不正"].append(tag)
        if it.get("answer") not in ("○", "×"): rep["answer欠落"].append(tag)
        for r in it.get("exam_refs") or []:
            if not REF_RE.match(r): rep["exam_refs形式"].append(f"{tag} : {r}")
        for f in ("question_text", "explanation_text"):
            fl = script_flags(it.get(f))
            if fl: rep["文字種"].append(f"{tag} [{f}] {sorted(fl)}")
        if it.get("confidence") in ("low", "medium") or it.get("uncertain"):
            rep["要目視確認"].append(f"{tag} conf={it.get('confidence')} {it.get('uncertain')}")

    # 肢番号の連続性
    grp = collections.defaultdict(list)
    for it in items:
        grp[tuple(it.get("heading_path") or [])].append(it)
    for h, lst in grp.items():
        nums = [x["stmt_no"] for x in sorted(lst, key=lambda x: (x.get("pdf_page_q") or 0)) if x.get("stmt_no")]
        for a, b in zip(nums, nums[1:]):
            if b not in (1, a + 1) and not (b <= a):  # 番号が飛ぶ(リセットは許容)
                rep["肢番号の欠番"].append(f"{'/'.join(h)}: {a}→{b}")

    # oneliner.json との照合
    ol_path = os.path.join(REPO, "data", "oneliner.json")
    if os.path.exists(ol_path):
        ol = json.load(open(ol_path, encoding="utf-8"))
        by_ref = collections.defaultdict(list)
        for o in ol:
            for c in o.get("year_codes") or []:
                by_ref[c.replace("·", "・")].append(o)
        matched = 0
        for it in items:
            cands = {id(o): o for r in (it.get("exam_refs") or []) for o in by_ref.get(r.replace("·", "・"), [])}
            if not cands or not it.get("question_text"): continue
            q = norm(it["question_text"])
            best = max(((difflib.SequenceMatcher(None, q, norm(o["question"])).ratio(), o) for o in cands.values()),
                       key=lambda x: x[0])
            if best[0] >= 0.98: matched += 1
            elif best[0] >= 0.75:
                rep["oneliner照合:ほぼ一致(誤認識候補)"].append(
                    f"#{it['seq']} p{it.get('pdf_page_q')} ratio={best[0]:.3f}\n  book: {it['question_text'][:80]}\n  onel: {best[1]['question'][:80]}")
        rep["_info"].append(f"oneliner完全一致(>=0.98): {matched}件")

    lines = [f"# 検証レポート(items={len(items)})", ""]
    for k, v in rep.items():
        lines.append(f"## {k}({len(v)}件)")
        lines += [f"- {x}" for x in v[:300]]
        if len(v) > 300: lines.append(f"- …ほか{len(v)-300}件")
        lines.append("")
    p = os.path.join(ROOT, "out", "report.md")
    open(p, "w", encoding="utf-8").write("\n".join(lines))
    print("\n".join(f"{k}: {len(v)}" for k, v in rep.items()))
    print("->", p)

if __name__ == "__main__":
    main()
