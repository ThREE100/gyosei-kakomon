"""巨大PDF(100MB超はClaude CodeのReadで読めない)を、ページごとのJPEG画像に分割する。

  pip install pymupdf
  python prep-pages.py book.pdf --start 40 --end 60 --dpi 200

出力: work/pages/p0040.jpg ... (PDFのページ番号=ファイル名の番号、1始まり)
既にあるページはスキップする(再開可能)。
"""
import argparse, os, sys
try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("PyMuPDF が必要です: pip install pymupdf")

ap = argparse.ArgumentParser()
ap.add_argument("pdf")
ap.add_argument("--start", type=int, default=1)
ap.add_argument("--end", type=int, default=0, help="0=最終ページまで")
ap.add_argument("--dpi", type=int, default=200)
ap.add_argument("--quality", type=int, default=85)
a = ap.parse_args()

root = os.path.dirname(os.path.abspath(__file__))
outdir = os.path.join(root, "work", "pages")
os.makedirs(outdir, exist_ok=True)
doc = fitz.open(a.pdf)
end = a.end or doc.page_count
print(f"pages in pdf: {doc.page_count}")
for n in range(a.start, min(end, doc.page_count) + 1):
    p = os.path.join(outdir, f"p{n:04d}.jpg")
    if os.path.exists(p):
        continue
    pix = doc[n - 1].get_pixmap(dpi=a.dpi, colorspace=fitz.csRGB)
    pix.save(p, jpg_quality=a.quality)
    if n % 20 == 0:
        print("saved", n)
print("done ->", outdir)
