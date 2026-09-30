# 過去問集PDF(1060ページ)→ 構造化JSON 抽出ツール

市販書籍(TAC合格革命 行政書士 分野別過去問集2026)のPDFを、Windows(PowerShell)上の Claude Code で
ページ範囲ごとに読み取り、**構成(科目>章>節>項>肢、ランク、出題履歴、正誤、解説)を保った**JSONにする。

> **著作物の扱い**:PDFと出力(`work/`・`out/`)は**このリポジトリ(公開)に入れない**。`.gitignore`で除外済み。
> 出力は非公開の場所(ローカル、または非公開リポジトリ)に置く。コミットするのはスクリプト・プロンプトのみ。
> 動作確認はダミーデータでのみ実施。**実物のPDFでの精度は未検証**のため、必ず試験運用(手順2)から始める。

## 構成

| ファイル | 役割 |
|---|---|
| `prompts-extract.md` | 抽出プロンプト(JSONの形式・転記ルール。逐語転記、読めない字は〓、下線は`<u>`) |
| `prep-pages.py` | PDFをページ別JPEG(`work\pages\pNNNN.jpg`)に分割。**100MB超のPDFはClaude CodeのReadで読めないため必須** |
| `run-extract.ps1` | ページ画像を`-Chunk`枚ずつ(既定6、重なり1)`claude -p`に渡し、`work\chunks\`にJSONを保存。既存はスキップ=再開可能、JSON不正は再試行 |
| `merge.py` | チャンクを見出し階層(`heading_path`)付きで統合し`out\book.json`へ。重なりページの重複を除去 |
| `validate.py` | 形式・文字種(簡体字・〓・ハングル等)・肢番号の欠番・`data/oneliner.json`との照合・要目視確認を`out\report.md`へ |

## 手順(PowerShell)

前提:Claude Code がインストール済み、Python 3 が使えること。このリポジトリを`git pull`して`tools\kakomonshu-extract`へ移動。
出力先(`work\`・`out\`)をこのフォルダ以外にしたい場合は、フォルダごと非公開の場所へコピーして実行してよい。

1. **目次ページを確認**:PDFの何ページ目から本文が始まるか、目次は何ページかを確認する。
2. **試験運用(20〜30ページ)**:
   ```powershell
   pip install pymupdf                                   # 初回のみ
   python prep-pages.py book.pdf --start 40 --end 60     # PDF→ページ画像(work\pages)
   .\run-extract.ps1 -Start 40 -End 60 -Chunk 6 -Overlap 2
   python merge.py
   python validate.py
   ```
   `out\report.md` と、元PDFの該当ページを見比べる。見るポイント:
   - 肢の取りこぼしがないか、問題側と解説側の対応(○×)が合っているか
   - 見出し階層(`heading_path`)が正しいか
   - 簡体字混入・誤認識(レポートの「文字種」「oneliner照合」)がどれくらい出るか
   - 1チャンクの所要時間と、Claude の利用量(上限に当たらないか)
3. 結果に応じて `prompts-extract.md` を調整(必要なら`-Chunk`を4や8に)。**プロンプトを変えたら`work\chunks`の該当ファイルを消して再実行**。
4. **本番**:
   ```powershell
   python prep-pages.py book.pdf          # 全ページを画像化(時間がかかる)
   .\run-extract.ps1 -Start 1 -End 1060 -Chunk 6 -Overlap 2
   ```
   PowerShellウィンドウを複数開き、ページ範囲を分けて並列に実行してもよい(出力ファイル名が範囲ごとに分かれるため衝突しない)。
   Claude Code の利用量制限に当たったら、時間をおいて同じコマンドを再実行(完了済みはスキップされる)。
5. `python merge.py` → `python validate.py`。`report.md`の要確認リストを、PDFの該当ページと見比べて修正する。
6. (精度をさらに上げる場合)**副系統OCR**(GPU使用、YomiToku等の日本語特化OCR)の本文と`book.json`を突き合わせ、
   不一致箇所だけを再読させる。試験運用の結果、Claude単独の誤り率が高い場合に追加する。

## 出力の形(`out\book.json`)

```
{ "meta": {...}, "headings": [{level,text,pdf_page,path}], 
  "items": [{ seq, heading_path[科目,章,節,項], rank, exam_refs[], original, stmt_no,
              question_text, answer(○/×), explanation_text, pdf_page_q, pdf_page_a,
              confidence, uncertain[] }],
  "other": [{ kind: toc|preface|column|table|figure|note, text, pdf_page }] }
```

`pdf_page_q`/`pdf_page_a`で必ず原本のページに戻れる。

## 既知の制約・注意

- Claude Code のReadツールは**100MBを超えるPDFを読めない**(実機で確認)。そのためPDFを画像に分割して読ませる。1回に読むのは6ページ分の画像で、精度を優先している。
- 問題ページと解説ページが離れている場合、`-Overlap`で重なりを持たせて拾う。それでも対応が取れない肢は
  `answer:null`・`uncertain`付きで残り、`report.md`の「answer欠落」に出る。
- 下線・太字は`<u>`・`<b>`で保存(暗記マーカーの情報を落とさないため)。
- `validate.py`の簡体字リストは代表例であり、網羅ではない。
