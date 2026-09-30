# 問題別インフォグラフィック プロンプト作成ルール（固定テンプレート）

## これは何か

`format-template.md` に沿って書いた1問1答の解説記事（例：`r3-mondai/q09-chiban-kaokubangou.md`）の内容をもとに、その問題全体（通常ア〜オの5肢）の要点を1枚で俯瞰できる**インフォグラフィック**を作るための、画像生成プロンプトを組み立てる手順を定める。

画像生成そのもの（ChatGPTのGPT Image 2等）はユーザーが手動で行う。このリポジトリ・このルールで作るのは**プロンプトの文章まで**であり、画像ファイルは生成しない。

## 対象と非対象（他のルールとの切り分け）

インフォグラフィック関連の成果物は5種類あり、混同しないこと。

| 種類 | 対応するルール | 内容 | スタイル | サイズ |
|---|---|---|---|---|
| ①肢ごとの note見出し画像 | このドキュメントの対象外（都度チャットで個別に作成） | 1つの肢(ア〜オのうち1つ)の結論を1シーンで表現 | フルカラー・淡いパステルカラーのアイソメトリック・フラットデザイン（2026-09-14訂正、下記「見出し画像のスタイル訂正」参照） | 1280×670px 横長固定 |
| ②問題全体のインフォグラフィック | **このドキュメント** | その問題の5肢すべてを俯瞰する複数パネル構成 | カラー・フラットデザイン・アイソメトリック(斜め見下ろし)アイコン | 縦長ポートレート(下記「サイズ」参照) |
| ③分野別・個別テーマ記事のインフォグラフィック | **このドキュメントの「③ 分野別・個別テーマ記事」章**（2026-08-06〜プロンプト化） | 記事1本につき**複数枚**のプロンプト（俯瞰ポスター・対比表・早見表・フローチャート等、必要な枚数だけ） | ②と同じ画風を基本とし、画像の種類に応じて表・フロー等のレイアウトも許容 | 画像ごとに内容量に応じて決定 |
| ④間違いノート型（特定の肢の深掘り解説） | **このドキュメントの「④ 間違いノート型」章**（2026-08-24〜） | 読者が正誤を自力で導けなかった**特定の肢1つ**について、つまずきやすい思考の癖を可視化する解説図解 | ②③と同じ画風を基本としつつ、**文字量・説明文の制限を撤廃**（フローチャート・比較図・長めの注釈可） | 画像ごとに内容量に応じて決定 |
| ⑤作図ガイド型（問題全体の思考順序） | **このドキュメントの「⑤ 作図ガイド型」章**（2026-09-14〜） | 問題文を読んだときに**5肢すべてについて**実際に手を動かして描くべき図と、その図にたどり着くための判定順序（フローチャート的な思考手順）を示す解き方ガイド | ②③と同じ画風を基本としつつ、④と同様に**文字量・説明文の制限を撤廃**（着眼点の説明文・条件分岐を明記可） | 画像ごとに内容量に応じて決定（目安1080×2600px） |

このドキュメントは②・③・④・⑤を対象とする。①の依頼が来た場合のみ、これまで通り個別にプロンプトを作る（このドキュメントの対象外）。ただし、下記「背景の不透明化（必須・厳守）」は①を含む5種類すべてに例外なく適用する（①は固定雛形を使わないため、プロンプト作成時に手動で文言を追記すること）。

**④と⑤の違い（重要）**：④は読者から「特定の1肢の結論に自力でたどり着けなかった」というフィードバックがあった場合に、その1肢だけを深掘りする**事後対応**。⑤は読者からのフィードバックの有無にかかわらず、**問題全体（通常5肢）**について「そもそも読んだ瞬間にどう図を描き、どの順番で条件を確認すればよいか」を示す**予防・練習素材**であり、②のカードポスターを作成する際に併せて（または後から）用意することを基本とする。

**2026-08-06付の変更**：従来、`bunya-kaisetsu/format-template.md`（2026-09-18に`topics/`へ統合され廃止）の「インフォグラフィック設計メモ」は文章のみで構成案を指定し、プロンプト化はしない運用だった。この運用を改め、③（分野別・総合記事、および `topics/` の個別テーマ記事）についても、②と同じ基本ルール（縦長ポートレート・フラットデザイン・アイソメトリック・カード構成・簡体字対策・verbatim厳守）を引き継いだうえで、実際に画像生成に使える**プロンプト文**として記事に記録する運用に統一する。具体的なルールは本ドキュメント末尾の「③ 分野別・個別テーマ記事のインフォグラフィック プロンプト作成ルール」を参照。

## 手順（問9で行った作業の再現）

1. **対象記事を読む**：`note-articles/{年度}-mondai/q{n}-*.md` を読み、以下を抽出する。
   - 記事タイトル・分野テーマ（例：「地番と家屋番号の基本ルール」）
   - 出題年度・問題番号（記事冒頭の「出題年度：」行、またはファイル名から特定する。例：「平成21年度 午後の部 第1問」）
   - 各肢（ア〜オ）の「まとめ表」の1行分（判定＋ポイント）と、本文の結論部分
   - 全体を貫く軸（例：「土地の地番に関する原則」と「建物の家屋番号に関する原則」で2系統に分かれる）があれば、それをレイアウトの列・グループ分けの基準にする
2. **正しい結論だけを図解する**：問題文の「誤っている記述」をそのまま図解しない。まとめ表で「誤」と判定された肢は、正しいルール（＝その肢が本当は何と言うべきだったか）に直して図解する。（例：問9のイ「登記官は地番を変更できない」は誤りの肢だが、インフォグラフィックには正しいルール「地番が錯雑している場合、登記官は職権で変更できる」として載せる。）
3. **カードに落とし込む**：抽出した内容を、原則ごとに1枚の「カード」（番号バッジ＋見出し＋図解＋結論タグ）にする。1カード＝1肢が基本だが、テーマが近い肢は1カードにまとめてもよい。カード数の目安は4〜6枚（肢の数と一致させる必要はない）。カードの番号は列ごとにリセットせず、1枚目から通し番号（1・2・3・4・5…）を振る。
4. **各カードに次の4要素を用意する**：
   - 番号バッジ（通し番号。列ごとに色を変える。例：列A＝緑の丸、列B＝青の丸。列見出しの色と揃える）
   - 見出し（1行、太字、体言止めまたは短い文で結ぶ。**20字前後を上限とする要約フレーズにする**。まとめ表のポイント欄をそのまま使わず、主語や条文番号を落としてさらに削ぎ落とす。「〜ないと確認」「〜ると確認」のように完結した1文にそのまま「と確認」を継ぎ足す書き方は不自然になるため避ける。詳細は「⑤ 作図ガイド型」章の「Headingの自然な日本語チェック」を参照）
   - 図解の説明（構図・アイコン・ラベルに使う文字列を具体的に指定する。誰が読んでも同じ絵になる粒度で書く。○×マーク・チェックマーク・短いラベル札は図解の中に直接埋め込む）
   - **結論タグ**（図解の下に置く、色付きの帯・バッジに入れる**5〜15字程度の一言**。文章ではなく単語・短フレーズにする。例：「移転登記が先」「家庭裁判所の許可 不要」「承諾だけでは不可」「表示登記」「転写されないだけ」。条文番号や「〜であり、〜とされていない」のような説明文はここに入れない）
5. **下記「プロンプト雛形」に流し込み、プロンプト文を完成させる。**
6. **完成したプロンプト文だけをユーザーに提示する**（画像は生成しない）。

### 見出し・結論タグを「要約」する具体例（重要）

まとめ表のポイント欄や本文の結論は、条文根拠つきの1文になっていることが多い。これをそのままカードの見出し・結論タグに転記すると文字だらけになるため、**この段階で必ず圧縮する**。

| 元の文（まとめ表・本文） | 見出し（20字前後） | 結論タグ（5〜15字） |
|---|---|---|
| 分筆の登記を申請できるのは、表題部所有者または所有権の登記名義人に限られる（不動産登記法39条1項）。名義変更前の買主は単独では申請できない。 | 名義変更前の買主は申請不可 | 移転登記が先 |
| 分筆の登記は財産の現状を大きく変える処分行為ではなく管理行為的なものとされ、相続財産管理人による申請に家庭裁判所の許可を証する情報の提供は不要。 | 相続財産管理人は許可不要 | 家庭裁判所の許可 不要 |
| 分筆の登記は表示に関する登記であり、賃借権の登記名義人の承諾を証する情報は添付情報とされていない。 | 賃借権者の承諾は不要 | 表示登記 |

条文番号（「不動産登記法39条1項」等）は見出し・結論タグには含めない。根拠を残したい場合は、図解内のごく小さな注記（誰も読まなくても構成が崩れない程度の補助情報）にとどめ、主役にしない。

## プロンプト雛形（固定フォーマット）

```
Create a Japanese-language infographic, portrait layout, {SIZE_PX} pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, beige, gray), rounded card sections, consistent with a
modern explainer-graphic aesthetic (icons: isometric buildings, land
plots, stamps, torn paper labels, etc. — adapt icon set to the topic).

GLANCEABLE-POSTER REQUIREMENT (critical): This is a quick-reference poster,
NOT a text-heavy explainer document. There is NO intro illustration and NO
paragraph of prose anywhere on this poster — go straight from the header
to the cards. Every card must communicate its point almost entirely
through the illustration (icons, X marks, checkmarks, small embedded
labels) plus one short heading and one short conclusion tag. Do NOT render
any full-sentence explanation, legal citation, or paragraph of body text
anywhere on the poster. If a piece of information cannot be expressed as a
short label (a few words) or drawn as an icon, leave it out rather than
writing it as prose.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters (traditional hanzi) either, even where a traditional-hanzi
glyph looks close to the correct Japanese kanji form — every glyph must
match the standard Japanese Jōyō form exactly, not the Chinese
traditional variant. Do NOT render any character that is not standard
Japanese hiragana, katakana, or Jōyō kanji anywhere in the image —
no Chinese-only characters, no Korean Hangul, no other non-Japanese
script, and no stray or decorative glyphs of any kind, even as small
background or texture elements. Every kanji must match standard Japanese
orthography exactly as written below, stroke-for-stroke. Reproduce the
exact text strings given below verbatim — do not paraphrase, translate,
summarize, or substitute any characters.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances, even if the output file format
supports transparency. Fill the full canvas — including every corner and
margin outside the cards/columns — with a solid or illustrated opaque
background (the pale beige/gray tone used elsewhere in this style is a
good default). There must be no checkerboard pattern, no partially
transparent area, and no unpainted canvas edge anywhere in the final
image.

--- HEADER ---
Title (large, bold, {N}行):
{TITLE}

Subtitle (smaller, centered, {N}行):
{SUBTITLE}

（タイトル・サブタイトルのすぐ下にカード群を続ける。導入イラスト・導入文の
ブロックは置かない。{SUBTITLE}は「テーマの要約フレーズ(◯◯年度 午後の部 第N問)」
の形式とし、必ず末尾に出題年度・問題番号を半角括弧で付記する。テーマの要約
フレーズだけで出題年度・問題番号を省略しない。）

**{SUBTITLE}に正誤の結論を書かない（重要・厳守）**：{SUBTITLE}は年度・問題番号と、
分野・論点を要約したテーマの一言にとどめる。「正しい肢はイ・ウ」「誤っている肢は
ア・エ・オの3個」のように、どの肢が正しい/誤りかという**結論そのもの**をサブタイトル
に書いてはならない。年度・問題番号の後ろに付け加える要素が思いつかない場合は、
無理にテーマの一言を足さず、年度・問題番号だけ（例：「令和7年度 午後の部 第10問」）
で済ませてよい。

--- COLUMN A HEADER (pill-shaped badge, color: {COLUMN_A_COLOR}) ---
{COLUMN_A_LABEL}

--- COLUMN A, CARD {N} ---
Badge: a filled circle in {COLUMN_A_COLOR} containing the number {N} (numbers
run continuously across all columns — do not restart at 1 in column B).
Heading (bold, ONE line, ~20 Japanese characters or fewer — a compressed
takeaway phrase, not the original full sentence from the article):
{CARD_HEADING_SHORT}
Illustration: {CARD_ILLUSTRATION_DESC} (embed any ✕/✓ marks and short
name-tag labels directly inside the illustration itself, e.g. a crossed-out
document icon with a 2-4 character label next to it)
Conclusion tag (a short colored banner/pill directly below the illustration,
{COLUMN_A_COLOR}, 5-15 Japanese characters, a keyword phrase — NOT a
sentence, NOT a legal citation):
{CARD_CONCLUSION_TAG}

（…カードの数だけ繰り返し。列を分けない場合は「COLUMN」を省略して1列で並べ、
バッジ色は1色に統一する。）

--- FOOTER ---

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional
Chinese. If any character renders as a Simplified or Traditional Chinese
variant, redraw that character in the correct Japanese form. Also scan
the entire canvas for any character that is not standard Japanese
hiragana, katakana, or Jōyō kanji — including any Chinese-only character,
Korean Hangul, other non-Japanese script, or stray decorative glyph — and
remove or redraw it so that only standard Japanese text appears anywhere
in the image. Confirm the number of cards equals {CARD_COUNT}
exactly, with no duplicated or missing cards, confirm there is no intro
illustration or paragraph block between the header and the cards, confirm
that no card contains a full sentence of explanatory prose — every card's
takeaway must read as a short heading + a short conclusion tag, at a
glance — confirm nothing is rendered below the last card (no summary
recap panel, no trophy or medal icon, no re-listed ○/✕ grid of all 肢,
and no additional text block of any kind — the poster ends immediately
after the last card), and confirm the entire canvas, edge to edge, is
filled with a fully opaque background with no transparency or alpha
channel anywhere.
```

**イントロブロック禁止（重要・厳守）**：かつてこの雛形には「--- INTRO BLOCK (left: illustration; right: paragraph text) ---」として、タイトル直下に導入イラストと数行の解説文を置くセクションが存在したが、廃止した。タイトル・サブタイトルのすぐ下は必ずカード群（`--- CARD 1 ---` またはコラムがある場合は `--- COLUMN A HEADER ---`）から始めること。導入イラスト・導入文のブロック、及びそれに類する説明段落（分野紹介・全体像の要約文など）は、HEADERとカード群の間は言うまでもなく、CRITICAL TEXT REQUIREMENTの直後からHEADERまでの間にも置かない。カードの通し番号列挙リストや簡体字注意文などの補足情報は、HEADERより前ではなく、FOOTER直前（Final checkの前）にまとめる。**このとき、独立した日本語の一文（「注意：〜」等）としてFOOTERに置いてはならない（重要・厳守、下記「簡体字注意文の画像内描画事故（2026-09-11判明）」参照）。** 必ず英語で書き、`Final check before rendering:` の英文パラグラフの一部として一体化させること。

**アウトロブロック禁止（重要・厳守、2026-09-16追加）**：カード群（②③の「俯瞰カードポスター型」「対比表型」「早見表型」「フローチャート／判定フロー型」、④のパネル、⑤のパネル）の最後の要素（最後のカード／最後のパネル／表の最終行）のあとは、必ずFOOTERの`Final check before rendering:`パラグラフだけを置く。画像生成AIが指示していないにもかかわらず、最後のカードの下に「正解のまとめ」「トロフィー・メダルのアイコン付きの正誤一覧」「肢ごとの○×を再掲するグリッド」といった**独自の追加サマリーパネル**を描き足してしまう事故が実際に発生した（ユーザー提示のスクリーンショットで確認）。これを防ぐため、`Final check before rendering:`パラグラフに、「最後のカード／パネルの後には、追加のサマリーパネル・トロフィーやメダルのアイコン・正誤を再掲する○×グリッド・その他いかなる文字ブロックも描画しない（confirm nothing is rendered below the last card/panel — no summary recap panel, no trophy or medal icon, no re-listed ○/✕ grid of all 肢, and no additional text block of any kind）」という趣旨の一文を必ず含める。過去に作成したプロンプトにこの一文がない場合は、発見しだい追記する。

**簡体字注意文の画像内描画事故（2026-09-11判明・再発防止）**：FOOTER直前に「注意：特に「共」「担」「保」…の各漢字は、簡体字ではなく標準的な日本語の常用漢字の字形で描画すること。」のような、独立した日本語の注意喚起文を1文だけ置く運用を一部の記事で行っていたところ、画像生成AIがこの文自体を**指示ではなくポスター上の可視テキストとして描画してしまう**事故が実際に発生した（ユーザー提示のスクリーンショットで確認）。原因は、この注意文が日本語であるため、プロンプト中の他の「そのまま描画すべき日本語ラベル」と区別がつかず、画像生成AIに指示ではなく描画対象の文字列として解釈されたことにある。英語で書かれた`Final check before rendering:`以降の段落は指示文として認識され描画されない一方、独立した日本語の一文はその保護を受けられない。**再発防止策**：漢字個別の注意喚起は、独立した日本語の文としてプロンプトのどこにも置かず、必ず英語の`Final check`パラグラフに埋め込む（例：`Final check before rendering: scan every kanji glyph, paying special attention to 共・担・保・録・登・記・筆・仮, and confirm each is in standard Japanese (Jōyō) form, not Simplified Chinese.`のように、漢字リストを英文の一部として文中に挿入する）。過去に作成した記事のプロンプトでこのパターン（FOOTER直前の独立した日本語「注意：」文）が見つかった場合は、発見ししだいこの形式に修正する。

## 文字化け・簡体字対策（必須・厳守）

問9のインフォグラフィックで実際に発生した不具合（簡体字混入、用語の誤変換「公溜地（溜池）」「公園用地」、見出しの重複「墓地」、判読不能な文字列「/港口用用」）を再発させないため、以下を必ず守る。

**2026-09-23追加（対象を繁体字・非日本語文字全般に拡大）**：簡体字だけでなく繁体字（Traditional Chinese）の混入、および日本語（ひらがな・カタカナ・常用漢字・算用数字）以外の文字（英字・ハングル・判読不能な疑似文字列等）が背景・枠・装飾等のどこかに紛れ込む事故も同様に発生しうるため、以下1〜6の「簡体字」に関する記述は、雛形の CRITICAL TEXT REQUIREMENT・Final check の文言と同様に、繁体字・非日本語文字全般の禁止も必ず含めて運用する。

1. プロンプトの冒頭と末尾の二重で「日本語のみ・常用漢字のみ・簡体字禁止・繁体字禁止・日本語以外の文字（英字・ハングル等）の混入禁止」を明記する（雛形の CRITICAL TEXT REQUIREMENT と Final check の両方を必ず含める）。
2. カード見出し・結論タグ・ラベルに使う文字列は、圧縮後（上記「見出し・結論タグを『要約』する具体例」参照）に確定した文字列をプロンプト側でそれ以上言い換えない。プロンプト自体にも「verbatim（そのまま）・do not paraphrase」と明記する。
3. 列挙型の要素（種類の一覧など、項目数が決まっているもの）がある場合は、番号付きリストで全項目を一字一句明記し、「重複禁止・欠落禁止・言い換え禁止」を明記したうえで、生成後に個数と内容を自己検証させる一文を末尾に追加する。この列挙リストも、HEADERより前ではなくFOOTER直前に置く（上記「イントロブロック禁止」参照）。
4. 特に誤りやすい漢字（号・録・権・地・番・建・物・登・記・所・請・還など、簡体字との字形差が大きい字）がプロンプトに含まれる場合は、名指しで「簡体字にしない」よう注意喚起する一文を添える。**この注意喚起は、独立した日本語の一文としてFOOTERやプロンプト中に置いてはならず（重要・厳守）、必ず英語で書いて`Final check before rendering:`パラグラフの一部として一体化させること**（詳細・事故事例は上記「簡体字注意文の画像内描画事故（2026-09-11判明・再発防止）」参照）。この注意文自体に本物の簡体字（权・记など）を書かないよう特に注意する。
5. 生成後にユーザーが目視確認する前提だが、事前にこちらでも文字列の突き合わせ（記事本文とプロンプト中の文字列が一致しているか）を行ってから提示する。
6. **Final checkの注意喚起リストは、そのプロンプト自身に実際に登場する漢字だけを挙げる（重要・2026-09-19判明・再発防止）**：h17問3（付合・区分所有）の作図ガイドで、Final check段落が「償・益」に注意するよう指示していたが、この2字はプロンプト中のどこにも登場しておらず、逆に7回・2回登場していた「請」「還」（金銭請求・返還請求関連の頻出語）がリストから漏れていた事例が実際に発生した。他の記事のFinal check段落をコピーして使い回した際に、リストだけ差し替え忘れることが原因になりやすい。**リストを書く（または既存記事から流用する）たびに、リストに挙げた漢字がそのプロンプト本文に実際に含まれているか、逆に本文に頻出する誤りやすい漢字がリストから漏れていないかを、grep等で機械的に照合してから保存すること。**

## 背景の不透明化（必須・厳守）

画像生成ツール（ChatGPTのGPT Image等）は、背景を一部透過（アルファチャンネルあり）の状態で出力することがある。透過部分はnoteの記事本文やダークモード表示など、背景色が異なる環境に貼り付けた際に意図しない見え方になるため、**このドキュメントが対象とする②・③・④のすべての画像、および①（肢ごとの見出し画像、都度チャットで個別作成）についても例外なく**、以下を必ず守る。

1. プロンプトの中盤（CRITICAL TEXT REQUIREMENTの直後）と末尾（Final check）の二重で「背景は完全に不透明・透過禁止」を明記する（雛形の BACKGROUND REQUIREMENT と Final check の両方を必ず含める。②・③・④の各雛形にあらかじめ組み込み済み）。
2. 「transparent」「alpha channel」「透過」といった語を、禁止する対象として明示的にプロンプトへ書き込む（生成モデルに対して、格子模様（チェッカーボード）やアルファ抜きのキャンバスが許容されると誤解させないため）。
3. ①（個別の肢の見出し画像）のように固定雛形を使わず都度プロンプトを作成する場合も、このBACKGROUND REQUIREMENTの文言を必ず手動で追記する。
4. 生成後にユーザーが目視確認する前提だが、透過PNGとして出力されていないか（画像を異なる背景色の上に置いて確認する等）を生成物側でも確認するよう依頼文に添える。

## 正誤対比カードの○×指示の統一ルール（必須・厳守、2026-09-29判明・再発防止）

H24問5・問8・問9で、実際に生成した画像を確認したところ、「誤りやすい思い込み」と「正しいルール」を左右（または上下）に対比させるカード・パネルで、次の2種類の不具合が繰り返し見つかった。**このドキュメントが対象とする①〜⑤のすべての画像（②のカード、③の対比表型、④の間違いノート型、⑤の正誤対比型パネルを含む）で、対比カード・対比パネルを作成するたびに、以下を必ず確認すること。**

**不具合1：同じ箱に○と×を両方指示してしまう矛盾（H24問8肢エ・問9肢エで発生）**

「誤りやすい思い込み」の箱に「合筆できる（または印鑑証明書は必要）という緑チェックを描く」という指示と、「その箱全体を赤×で打ち消す」という指示を同時に書いてしまい、1つの箱に相反する2つのマークを要求する矛盾したプロンプトになっていた。画像生成モデルはこの矛盾を解消できず、結果として左右の箱が同じマーク（実例ではどちらも赤×）で描画されてしまった。

**不具合2：1〜2文字しか違わない近似テキストが複製されてしまう（H24問5肢オで発生）**

「精度区分　甲三まで」と「精度区分　甲二まで」のように、中央の1文字しか違わない2つの文字列を左右の看板に指示したところ、画像生成モデルが片方の文字列をもう片方に引きずられて複製し、両方とも同じ文字列（実例ではどちらも「甲二まで」）になってしまった。

**再発防止ルール**

1. **1つの箱・カードには○×どちらか一方のマークだけを指示する。** 「誤りやすい思い込み」の箱・「正しいルール」の箱、それぞれの説明文を書き終えたら、「checkmark」と「crossed out」「red ✕」の両方が同じ箱の説明の中に登場していないかを読み返して確認する。両方登場していたら、必ずどちらか一方だけに絞る。
2. **誤った思い込みが「できないことをできると誤解するもの」「不要な書類・手続を必要だと誤解するもの」の場合、○×の極性は左右で逆になる。** この場合、「誤りやすい思い込み」の箱には緑チェック（その誤解の内容そのものを表す）だけを描き、「正しいルール」の箱には赤×（実際にはできない／不要であること）だけを描く。極性が逆になるこのパターンでは、プロンプトの当該カード・パネルの冒頭に次のような一文を必ず添えて、生成モデルに左右を同じマークへ揃えさせないよう明示的に指示する。
   > IMPORTANT: the two sides must show OPPOSITE marks, not the same mark — this is a case where the mistaken belief predicts success/necessity (✓) but the actual rule says otherwise (✕); do not draw the same mark on both sides.
3. **誤った思い込みが「不十分な手段で目的の行為を試みて失敗する」パターン（例：証明情報の提供だけで合筆しようとして失敗する、分割登記だけで済ませようとして失敗する）の場合は、両方の箱がその「試み」自体に×を付けるだけでよく、チェックマークを混在させる必要はない。** この場合は極性の反転を意識する必要はなく、不具合1が発生しにくい構造である。どちらのパターンに当てはまるかを、書き始める前に判断する。
4. **左右（または上下）に並べる2つの文字列が1〜2文字しか違わない場合（例：「甲三まで」と「甲二まで」、「0.3ミリ以下」と「0.2ミリ以下」）は、次を必ず追加する。**
   - 「これら2つの文字列は同一ではない」ことを明記する一文。
   - 異なる文字（数字・漢字）を具体的に指定し、大きく・別の差し色で強調するなど、視覚的に区別しやすくする具体的な指示。
   - Final checkにも、この2つの文字列を個別に確認し、「同じ文字列になっていたら誤りであり、修正が必要」と明記する一文を追加する。
5. **カード・パネルを書き終えたら、「誤りやすい思い込み」側と「正しいルール」側（または左右の対比）を声に出して読み比べ、実際に生成される2つの絵が視覚的に異なるかどうかを自問する。** 「両方とも同じ結論のマーク・同じ文字列になっていないか」を必ず確認してから次のカード・パネルに進む。

## サイズ・アスペクト比

- 問題全体のインフォグラフィック（このドキュメントの対象）は、カード数が多く情報量が多いため**縦長ポートレート**を基本とする。目安は `1080×1920px`（9:16）だが、カード数が多い／少ないなど内容量に応じて `{SIZE_PX}` は調整してよい。ユーザーから明示的な指定があればそれを優先する。この画像はnoteの「見出し画像」枠には設定せず、記事本文中に挿入する図解として使う（下記の理由により、見出し画像の推奨比率とは大きく異なるため）。
- 肢ごとの見出し画像（①、このドキュメントの対象外）は `1280×670px` 横長固定（アスペクト比1.91:1）。混同しないこと。この数値は、note公式ヘルプ「登録画像の推奨サイズ一覧」(https://www.help-note.com/hc/ja/articles/360000231642) に基づく、記事の見出し画像（サムネイル）の公式推奨サイズと一致している。同ヘルプによれば、登録画像が推奨サイズと異なる場合は自動的にトリミングされて表示されるため、見出し画像用に生成する画像は必ずこの比率(1.91:1)に合わせること。画像の最大容量は10MB。

### 見出し画像を実際にnoteへ設定する際の注意（note公式ヘルプに基づく）

- 見出し画像として使う画像は、上記の通り `1280×670px`（比率1.91:1）で生成・トリミングすること。この比率からずれた画像をそのままnoteに登録すると、note側で中央部分だけが自動的に切り出され、意図した構図（例：キャラクターや吹き出しの位置）がずれて表示されるおそれがある。
- より高精細に表示したい場合は、同じ比率のまま `1920×1006px` で用意してもよい（note公式ヘルプが挙げる「よりきれいに表示する」ためのサイズ）。
- ブラウザとアプリでは見え方が異なる点、また一覧ページでは `1280×454px` の範囲のみが表示される点も踏まえ、画像の主要な要素（キャラクター・吹き出し・タイトル文字など）は画像の中央付近に収まるよう構図を作ること。

## スタイル（問9・問11で確立した基準）

- カラー：淡いパステルカラー（青・緑・ベージュ・グレー）のフラットデザイン
- アイコン：アイソメトリック（斜め見下ろしの3D風）
- 構成：タイトル(上部) → サブタイトル → 複数カラムの原則カード群 → フッター（導入イラスト・導入文のブロックは置かない。タイトル直下からすぐカードに入る）
- **カードは「読ませる」のではなく「見せる」**：各カードは通し番号バッジ＋短い見出し(1行)＋図解＋短い結論タグ(5〜15字)の4点のみで構成し、説明文・条文根拠を長文で書かない。図解の中の○×マークや短いラベル札で情報を伝える。
- 列ごとに色を割り当て（例：列A＝緑、列B＝青）、その列の見出しバッジ・カード番号バッジ・結論タグの色を統一する。
- 肢ごとの見出し画像も、②③④と共通のフルカラー・パステル・アイソメトリックのビジュアル言語で統一する（下記「見出し画像のスタイル訂正」参照）。

### 見出し画像のスタイル訂正（2026-09-14実施）

上記「①肢ごとの note見出し画像」は、かつて「モノクロ鉛筆画、女性キャラクター1人が資料を持つ構図」と記載していたが、これは実際の運用（`mistake-notebook-magazine.md`のマガジンヘッダー仕様や、実際にユーザーが生成・使用している見出し画像）と一致しておらず、古い段階の記述が更新されずに残っていたものと判明したため、以下のとおり訂正する。

- **正しい現行スタイル**：フルカラー、淡いパステルカラー（青・緑・ベージュ・グレー等）のアイソメトリック・フラットデザイン。②③④の問題別・分野別インフォグラフィックと同じ画風を基本とする。
- モノクロ鉛筆画・特定の女性キャラクターを描く、という指定は廃止する。人物キャラクターを入れるかどうか（カードのみのシンプル構成にするか、人物イラストを添えるか）は記事ごとに判断してよいが、色調・アイコンのテイストは②③④と統一すること。
- 過去にこの節を参照して「モノクロ鉛筆画」スタイルで作成した見出し画像がある場合、優先度は高くないが、機会があれば上記の現行スタイルに合わせて作り直すことが望ましい。

## 内容の正確性チェック

- インフォグラフィックに書く法的内容は、必ず元記事の「まとめ表」「各肢解説」と一致させる。独自解釈・誇張・簡略化しすぎた言い換えをしない。
- 元記事が後日修正された場合（例：R3午後第3問ウへの民法258条の2の追記）、インフォグラフィックのプロンプトも同じ内容に追従して更新する。
- 「誤っている肢」をそのまま図解しない（手順2を参照）。図解するのは常に「正しいルール」。

## 依頼を受けたときの実行手順（このルールの使い方）

「問{年度}{n}のインフォグラフィックのプロンプトを作って」と依頼されたら、次の順で対応する。

1. 対象記事（`note-articles/{年度}-mondai/q{n}-*.md`）を読み込む。
2. 上記「手順」1〜4に従い、カード内容を組み立てる。
3. 「プロンプト雛形」に流し込み、「文字化け・簡体字対策」「背景の不透明化」を必ず適用する（イントロブロックは置かない）。
4. 画像は生成せず、完成したプロンプト文だけをチャットに提示する。
5. ユーザーから求められない限り、記事ファイル自体（`.md`）は変更しない（このプロンプトはあくまで別途手動生成する画像の設計図であり、記事本文の一部ではない）。

---

## ③ 分野別・個別テーマ記事のインフォグラフィック プロンプト作成ルール

### これは何か

`topics/`（分野別・総合記事、および個別テーマ記事。地目23種類、筆界特定制度、表示登記の添付情報早見表、制限行為能力者総整理 等。2026-09-18に`bunya-kaisetsu/`を統合済み）、および `column/`（特定の1問に紐づかない概念解説・横断参照コラム。建物認定3要件、保存期間まとめ 等）を対象に、記事の内容を土地家屋調査士試験の初学者向けに視覚化する画像生成プロンプトを作成するルール。②（問題別）と違い、**1記事＝1枚に縛られない**。記事の構成（見出し・早見表・対比表）に応じて自然に分かれる単位ごとに、必要な枚数だけプロンプトを作る。

### ②との違い

- ②：1問（ア〜オ5肢）を1枚の俯瞰ポスターに圧縮する。
- ③：1記事（複数の見出し・複数の表を含むことが多い）を、内容量に応じて**複数枚**に分解してよい。上限は設けず、初学者の理解に資するなら何枚でも作成する。基本の画風・文字化け対策・正確性チェックのルールは②をそのまま引き継ぐ。

### 画像の「型」（4種類。記事の内容に応じて使い分ける）

1. **俯瞰カードポスター型**（②のスタイルをそのまま流用）：原則・ルールを4〜6枚のカードで並べる。②の「プロンプト雛形」をそのまま使う。テーマ全体の総論・まとめに向く。
2. **対比表型**：2つの制度・概念を左右（または上下）に並べて違いを視覚化する（例：土地の合筆の制限 vs 建物の合併の制限）。
3. **早見表型**：記事中のmarkdown表をそのまま画像化する（例：床面積の算入・不算入一覧、添付情報の要否一覧、届出先マトリクス）。行数が多い表は複数枚に分割してよい。
4. **フローチャート／判定フロー型**：「できる／できない」「課税／非課税」等を分岐させる判断樹形図（例：代位申請の可否、登録免許税の課税範囲の判定、筆界特定の却下事由）。

### 手順

1. 対象記事（`note-articles/topics/{slug}.md`、または `note-articles/column/{slug}.md`）を読み込む。
2. 記事の構成（大見出し・markdown表・早見表・対比構造）を洗い出し、画像に分解する単位を決める。目安：大見出し1つにつき1枚、markdown表1つにつき1枚。記事全体を俯瞰する扉絵的な1枚（俯瞰カードポスター型）を先頭に追加してもよい。
3. 各単位について、上記4つの「型」から最適なものを選ぶ。
4. 型に応じて②の雛形を流用・改変してプロンプト文を完成させる（下記「型別の雛形差分」を参照）。
5. 「文字化け・簡体字対策」「背景の不透明化」（いずれも②の章を参照）を必ず適用する。特に条文の号数・専門用語（地目23種類の名称、建物の種類の名称など列挙型の要素）を含む画像は、②のルール3（番号付きリストで一字一句明記し、重複禁止・欠落禁止・言い換え禁止を明記）を厳守する。
6. 記事本体の末尾（「見出し画像用フレーズ」ブロックの後、「対象とした過去問記事」リンク一覧の前）に、`## インフォグラフィック プロンプト` という見出しを立てる。画像ごとに `### 画像{n}：{内容が一目でわかる短い説明}` の小見出しを付け、コードブロック（\`\`\`）でプロンプト文を記録する。
7. 画像は生成しない。記事ファイルにプロンプト文を追記して保存するところまでが成果物（③は②と異なり、記事ファイルへの追記が成果物そのものである点に注意）。

### 型別の雛形差分

- **俯瞰カードポスター型**：②の「プロンプト雛形」をそのまま使う。
- **対比表型**：HEADERの後に `--- LEFT COLUMN ---` `--- RIGHT COLUMN ---` を設け、左右2列を明示する。対応する項目は同じ高さに配置し、対応する制限・要件が片方にしか存在しない場合は「該当なし」とグレーアウト表示するよう指定する。
- **早見表型**：`--- TABLE ---` セクションを設け、ヘッダー行（列名）と各データ行の文字列を一字一句明記し、"render as a clean flat-design table with alternating row background colors, Japanese sans-serif font, no monospace font" のように表としての描画を明示する。行数が多い場合は「1枚あたり最大6〜8行」を目安に分割し、画像タイトルに「(1/2)」等の通し番号を入れる。
- **フローチャート／判定フロー型**：`--- FLOWCHART ---` セクションを設け、開始ノード→分岐条件（ひし形アイコン）→結果ノード（○/×アイコン付き）という流れを、ノードごとに番号を振って明記する。

### 実行手順（このルールの使い方）

「{記事名}のインフォグラフィックのプロンプトを作って」と依頼されたら、次の順で対応する。

1. 対象記事を読み込む。
2. 上記「手順」1〜4に従い、画像単位・型を決める。
3. 型ごとの雛形にあてはめてプロンプト文を完成させる。
4. 「文字化け・簡体字対策」「背景の不透明化」を必ず適用する。
5. 記事ファイル末尾に `## インフォグラフィック プロンプト` セクションとして追記し、保存する。

---

## ④ 間違いノート型（特定の肢の深掘り解説）

### これは何か

読者から「まとめの正誤判定（正／誤）や結論には納得したが、なぜそうなるのか自力ではたどり着けなかった」というフィードバックがあった特定の肢について、その肢1つに絞って、つまずきやすい思考の癖（見落としがちな条件、直感に反する条文の要件、混同しやすい別制度との違い等）を可視化する解説図解。②・③が「網羅的に俯瞰する」ことを目的にしているのに対し、④は「1つの理解のつまずきを解消する」ことに特化している点が異なる。

### ②③との決定的な違い（重要・厳守）

②・③の「GLANCEABLE-POSTER REQUIREMENT」（カード内は短い結論タグのみ、フルセンテンスの説明文・条文引用禁止）は、④には**適用しない**。④は読者の理解を最優先するため、以下を明示的に許可する。

- フローチャート・decision tree形式で、分岐条件を文章で書いてよい。
- 比較・対比のために、条文の文言を（要約せず）そのまま引用してよい（本文中の判例・先例番号記載禁止ルールは④にも適用されるため、条文番号は書いてよいが判例・先例の番号は書かない）。
- 「誤りやすいポイント」「つまずきやすい理由」を、1〜3文程度の説明文として画像内に配置してよい。
- 1つの肢につき何枚作ってもよく、記事1本・1肢あたりの上限は設けない（通常は1枚で足りるが、内容が複雑な場合は分割してよい）。

ただし、④であっても以下は②③と共通して厳守する。

- 文字化け・簡体字対策（CRITICAL TEXT REQUIREMENT・Final checkの二重明記）
- 背景の不透明化（BACKGROUND REQUIREMENT・Final checkの二重明記。透過・アルファチャンネル禁止）
- verbatim厳守（指定した文字列をそのまま描画し、言い換えない）
- 元記事の本文・まとめの内容と矛盾する独自解釈を書かない
- 判例・先例・専門誌の具体的な番号は本文と同様に書かない（内容の言及は可）

### 画像の「型」

多くの場合、以下のいずれか（または組合せ）になる。

- **2段階フローチャート型**：「原則→例外」のように、複数の条件を順番に確認しないと正しい結論に至れない肢に向く（例：表意者の重過失があるか→相手方にも落ち度があるか、の2段階判定）。
- **対比型**：似た制度・条文と混同しやすい肢に向く（例：心裡留保の第三者保護要件と、詐欺の第三者保護要件の違い）。左右または上下に並べ、要求される要件の違いを明示する。

### 手順

1. 対象記事（`note-articles/{年度}-mondai/q{n}-*.md`）の該当する肢の解説を読む。
2. 読者がどこで判断を誤りやすいか（見落としがちな条件、直感的な誤読、類似制度との混同）を特定する。
3. 上記の型から最適なものを選び、分岐条件・比較項目を具体的に書き出す。
4. 下記の雛形に流し込み、文字化け・簡体字対策・背景の不透明化を適用する。
5. 記事ファイル末尾に `## インフォグラフィック プロンプト（{肢}肢・間違いノート）` として追記し、保存する。

### プロンプト雛形（間違いノート型）

```
Create a Japanese-language infographic, portrait layout, 1080x1920 pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, beige, gray), rounded panel sections, consistent with the
same visual language as the whole-problem poster for this article, but
built as a single detailed explainer panel rather than a multi-card
poster.

MISTAKE-NOTEBOOK EXPLAINER REQUIREMENT: This image exists to resolve one
specific point of confusion, not to be a glanceable summary. Unlike a
quick-reference poster, this image MAY include flowchart branches with
written conditions, side-by-side comparisons with quoted article text,
and short explanatory sentences (1-3 sentences per callout box) labeled
「誤りやすいポイント」or similar. Prioritize clarity and completeness of
the reasoning over brevity.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters (traditional hanzi) either, even where a traditional-hanzi
glyph looks close to the correct Japanese kanji form — every glyph must
match the standard Japanese Jōyō form exactly, not the Chinese
traditional variant. Do NOT render any character that is not standard
Japanese hiragana, katakana, or Jōyō kanji anywhere in the image —
no Chinese-only characters, no Korean Hangul, no other non-Japanese
script, and no stray or decorative glyphs of any kind, even as small
background or texture elements. Reproduce the exact text strings given
below verbatim — do not paraphrase, translate, summarize, or substitute
any characters. Pay special attention to the kanji {列挙する漢字} — always
draw the standard Japanese (Jōyō) form.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances, even if the output file format
supports transparency. Fill the full canvas — including every corner and
margin outside the panel/flowchart/comparison — with a solid or
illustrated opaque background. There must be no checkerboard pattern, no
partially transparent area, and no unpainted canvas edge anywhere in the
final image.

--- HEADER ---
Title (large, bold):
{タイトル：肢の結論を一言で}

Subtitle (smaller, centered):
{年度・問題番号・肢}－{つまずきポイントを一言で}

--- {FLOWCHART or COMPARISON} ---
{型に応じて分岐ノード／左右パネルを具体的に記述}

--- CALLOUT: 誤りやすいポイント ---
{1〜3文程度の説明文をverbatimで指定}

--- FOOTER ---
{条文番号等の小さな注記}

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional
Chinese. Also scan the entire canvas for any character that is not
standard Japanese hiragana, katakana, or Jōyō kanji — including any
Chinese-only character, Korean Hangul, other non-Japanese script, or
stray decorative glyph — and remove or redraw it. Confirm every
heading, node label, and callout text matches the Japanese text given
above verbatim, with no paraphrasing and no substituted characters,
confirm nothing is rendered below the FOOTER's small footnote text (no
summary recap panel, no trophy or medal icon, no re-listed ○/✕ grid, and
no additional text block of any kind), and confirm the entire canvas,
edge to edge, is filled with a fully opaque background with no
transparency or alpha channel anywhere.
```

---

## ⑤ 作図ガイド型（問題全体の思考順序をフローチャートで示す）

### これは何か

問題文（ア〜オ5肢）を読んだときに、実際に手を動かして描くべき図（家系図・登記記録・建物の位置関係など）と、その図にたどり着くまでに**どの順番で何を確認すればよいか**を、肢ごとに示す解き方ガイド。②の「結論カードポスター」が正誤の結論を俯瞰することに主眼を置くのに対し、⑤は「初見の問題文をどう思考順序に沿って図解し、正誤にたどり着くか」という**プロセスそのもの**を可視化する点が異なる。

R3午後第16問・R2午後第14問・R1午後第1問・H30午後第3問で確立した「作図ガイド」の運用を、正式な固定ルールとして整備したもの。

### ②③④との違い

- ②：5肢の**結論**を、文字数を絞ったカード（見出し＋短い結論タグ）で俯瞰する。GLANCEABLE-POSTER REQUIREMENTにより長文・条文引用は禁止。
- ③：1記事（複数の見出し・複数の表）を、内容量に応じて複数枚に分解する。②のスタイルを流用する「俯瞰カードポスター型」を含む4つの型から選ぶ。
- ④：読者から「特定の1肢の結論に自力でたどり着けなかった」というフィードバックがあった場合に、**その1肢だけ**を深掘りする事後対応。文字量制限はない。
- ⑤：フィードバックの有無にかかわらず、**5肢すべて**について「問題文を読んだ瞬間に何を図に描き、どの順番で条件を確認すればよいか」を示す予防・練習素材。④と同様に文字量制限はないが、④が「1肢の深掘り」であるのに対し⑤は「問題全体の解き方の型」を示す点で異なる。②のカードポスターとは別物として作成し、②の内容を書き換えない。

### 「フローチャート式」の考え方（重要・厳守）

⑤の核心は、単に完成した図（家系図・配置図など）を1枚見せることではなく、**その図に至るまでの判定順序**を読者に追体験させることにある。したがって、以下を必ず満たすこと。

1. **各肢の Diagram は、単なる完成図の説明ではなく、「まず何を確認し、次に何を確認し、最後にどう判定するか」という順序が読み取れる構図にする。** 具体的には、条件を1つずつ確認するステップを、上から下（または左から右）へ並べる、番号付きの確認ポイントを図の中に配置する、分岐が生じる場合は分岐点に○×の小さな判定マークを置く、といった手法を使う。
2. **複数の条件を順に満たさないと結論に至れない肢（原則→例外、多段階の要件判定など）では、Diagram を実際の決定木（フローチャート）として描く。** ひし形の分岐ノード、条件を書いたラベル、Yes/No（またはある/なし、○/✕）に応じた分岐矢印、最終的な結論ノードという構成要素を明示的に指定する。1段階の確認だけで完結する肢では、無理にフローチャート化せず、通常の図解（着眼点を絵で示す構図）でよい。
3. **着眼点コールアウトは、判定の「順番」を言葉でも明示する。** 「まず〜を確認します。次に〜を確認し、〜であれば…」のように、思考の手順が読み取れる文にする。結論だけを述べる文（②の結論タグのような一言）にしない。
4. **同じ記事内の複数肢を通して見たときに、共通する決定木の形（判定順序・分岐構造）があれば、その形を1つの雛形として使い回す。2肢のペアに限らず、3肢以上、あるいは5肢すべてが同じ木を共有してもよい（例：「除外事由①〜⑤のいずれかに該当するか」という同一の判定木を5肢すべてが共有し、各肢は自分が該当する枝だけを強調する構成、あるいは「死亡年月日→相続開始時点での生存確認→代襲原因の該当性」のような共通パターン）。共有木を使う場合は、各パネルで自分の肢に関係する分岐だけを太い縁取り・強調色ではっきり目立たせ、関係しない分岐は薄いグレーで縮小表示する（○×だけで済ませず、「今回は関係ない」ことが一目でわかる見た目にする）。
5. **一見1回のチェックで完結するように見える肢ほど、本文解説を読み直し、実際には2つ目の条件が隠れていないか疑う。** 隠れた条件がある場合は、それを無理に単純化せず、あえて2段階以上の決定木として可視化し、読者が見落としやすいポイントを図で示す（例：「妨害の有無」だけで足りるように見える肢が、実は「行政処分性」のような別条件も満たす必要がある場合）。逆に、本当に単一チェックで完結する肢を、無理に多段階のフローチャートへ仕立て上げてもならない。
6. **分岐点（ひし形ノード）の両方の結果が、そのルールを理解するうえで等しく重要な意味を持つ場合（例：「いずれか早い方が経過すると時効消滅する」という2本のタイマーの競争のように、はい側・いいえ側のどちらも読者が知るべき現実の結論である場合）、はい・いいえの両方の行き先を必ずプロンプトに明記する。** 令和5年度午後第1問パネル5（肢オ、取消権の消滅時効）の作図ガイドで、Diagramの記述が「はい」側（時効によって消滅する）の行き先だけを指定し、「いいえ」側の行き先を書いていなかったため、画像生成の結果、ひし形ノードから図の途中に不自然に戻ってしまうループ矢印が生成され、2本のタイマーのうち1本だけが再チェックされるかのような誤った・分かりにくい図になった実例が見つかった。このため、両方の結果が意味を持つ分岐点では、次を必ず守る。
   - 「いいえ」側にも、専用の結論ノード（「まだ消滅していない（取消権は存続）」等）を明記し、行き先を空白にしない。
   - 図中のどのノードにも戻る「ループ」矢印を描かせない（分岐点からは必ず新しい結論ノードへ進む）ことを、プロンプト内で明示的に禁止する。
   なお、その肢の問題文自体が「ある1つの事実（はい側）が成立している場面」を前提とする単一チェック型の肢（上記4項目目「無理にフローチャート化せず」の対象）では、いいえ側の結論が本文解説に存在しないことも多く、その場合まで無理にいいえ側を捏造する必要はない。上記の追記が必要なのは、あくまで両方の結果が本文解説上の実際の結論として存在する分岐点に限る。
7. **根拠条文・準則が長い列挙型（「〜を建物として取り扱うもの」「除斥事由は次の各号のいずれか」等）の場合、その列挙をそのまま分岐構造として図解しない。まず、その列挙が実は共通の一般原則（3〜4個程度の要件）を個別の具体例に当てはめているだけではないか（＝列挙は一般原則の適用結果の一覧にすぎないのではないか）を確認する。** 一般原則が存在する場合は、Diagramをその一般原則（どの要件を満たす／欠くか）を確認する図解に統一し、列挙の分類構造（「Aの例示に載っているか→ただし書きの条件があるか→条件を満たすか」のような何段にもわたる共有決定木）をそのまま再現しない。多くの肢は一般原則のうち1つの要件（またはその肢の結論を左右する1〜2要件）だけを確認すれば足りるので、無理に全要件を毎回確認させる多段階フローチャートに仕立てない（上記2・5項目目の「無理にフローチャート化しない／隠れた条件を疑う」のバランスを、列挙型の条文ではこの一般原則に照らして判断する）。同一テーマを扱う既存記事（同じ論点で先に作成済みの年度の⑤）があれば、その記事がどの一般原則・要素分解を採用しているかを確認し、揃える。
   - 実例（2026-09-25判明・改善）：平成19年度午前第19問（準則77条が列挙する「建物として取り扱うもの／取り扱わないもの」10例の認定）の作図ガイドで、当初は列挙をそのまま「Aの例示に載っているか→ただし書きの条件があるか→条件を満たすか」という11ノードの共有決定木として描き、これを10パネルすべてで再掲する設計にしていた。しかし、建物認定は本来、不動産登記規則111条・昭24.2.22民事甲240号による**定着性・外気分断性・用途性**という3要件の判定に帰着する分野であり（`note-articles/column/tatemono-nintei-3youken.md`参照）、令和4〜6年度・平成27年度・平成30年度の同テーマ⑤作図ガイドもこの3要件を判定軸に採用していた。列挙をそのまま分岐構造化した結果、パネルごとの図が不必要に複雑・深くなり（この実例のスクリーンショットで顕在化）、「読んだ瞬間に描ける図」という⑤の目的から外れていた。3要件を軸にした図解へ作り直したところ、複数要件の確認が本当に必要な2肢（3要件をすべて満たす典型例）だけを3段階の決定木にし、残り8肢は「結論を左右する1要件だけ」を確認する単純な図解に整理でき、プロンプトの分量もほぼ半減した。

### 法的正確性の担保（重要・厳守）

⑤は「わかりやすさ」を優先するあまり、対象記事の本文解説・まとめで既に確定している法的結論・要件を歪めてはならない。次を必ず守る。

1. **各パネルの Diagram・着眼点・結論タグに書く内容は、対象記事の本文解説・まとめで実際に使われている条件・結論と一致させる。** 図解作成の過程で、新しい法的主張・独自の言い換えによる結論の変更・条文の拡張解釈を持ち込まない。
2. **要件が複数の要素からなる場合（例：「善意」かつ「無過失」、「平穏」かつ「公然」）、図解の都合で1つの要素だけに圧縮しない。** 各要素を別々の確認ステップ（別のひし形ノードや別の着眼点の文）として描き分け、要素を落とすことで生じる誤解を防ぐ。
3. **パネルを書き終えたら、その肢の本文解説・まとめの記述と照らし合わせ、「この Diagram と着眼点は、本文のどの一文に対応しているか」を自分で説明できるかを確認する。** 対応する記述が本文に見当たらない内容は書かない。

### Headingの自然な日本語チェック（重要・厳守、2026-09-19判明・再発防止）

令和5年度午後第1問・第2問の作図ガイドで、Heading（パネルの短い見出し）が次のような不自然な日本語になっていた実例が見つかった。

- 「追認は過去にさかのぼらないと確認」
- 「取消しは過去にさかのぼると確認」
- 「請求先は補助者でなく本人と確認」

いずれも、「〜ない」「〜る」で終わる完結した1文に、そのまま体言止めで「と確認」を継ぎ足した形になっている。「を確認する」は「を確認」のように体言止めにしても自然だが（「有無を確認する」→「有無を確認」）、「〜と確認する」は「と」が発言・思考をそのまま受ける引用の助詞であるため、述語の「する」を落として「と確認」で止めると、文が尻切れになったように読めて不自然になる。この不具合を再発させないため、Headingは必ず次のいずれかの形にする。

1. **確認する対象を名詞句にして「〜の有無を確認する」「〜が〜かを確認する」の形にする**（例：「追認の遡及効の有無を確認する」「取消しに遡及効があるかを確認する」）。
2. **「確認」を使わず、ステップの内容を体言止めまたは短い文でそのまま言い切る**（例：「追認しても遡って有効化しない」「取消しは遡って無効になる」「占有補助者でなく本人に請求」）。

「完結した1文＋と確認」（「〜ないと確認」「〜ると確認」）という体言止めの継ぎ足しは書かない。また、「〜と確認する」を「する」まで書き切った場合でも、他のパネルが「〜の有無を確認する」「〜かを確認する」のような短い確認フレーズで統一されている記事内で、その1枚だけ「主語は〜できると確認する」のような一段長い完結文になっていないか（統一感を欠いていないか）もあわせて見る。Headingを書き終えたら、声に出して読んで不自然に感じないかを必ず確認する。

**もう1つの不自然パターン（2026-09-20判明・再発防止）**：令和6年度午後第1問の作図ガイドで、Headingが「知っていたかどうかは結論を変えない」となっていた実例が見つかった。これは文法的には誤りではないが、「誰が」「何を」知っていたのかという主語・目的語を省いた「かどうかは結論を変えない／影響しない」という抽象的な言い回しになっており、そのパネル単体では何の話かわからない見出しになっていた（他のパネルの見出しが「取消権の行使に同意はいらない」「日用品かどうかを先に見分ける」のように、そのパネルだけで具体的な内容がわかる自己完結した文になっているのと対照的）。この不具合を再発させないため、次を守る。

3. **Headingだけを読んで、その肢の主語・対象・結論が具体的にわかるようにする。** 「〜かどうかは結論を変えない／影響しない／関係ない」のように、判定対象（誰が・何を・どんな知識や状態を）を書かずに結果の抽象論だけを述べる書き方は避け、結論タグに書く具体的な結論（例：「知っても取消し可」）をHeadingにもそのまま組み込んだ短い文にする（例：「取消せると知っていても取消し可能」）。

### 画像の「型」

多くの場合、以下のいずれか（または組合せ）になる。①〜④は`note-articles/topics/`等で使われる語彙と共通するため、③の「型別の雛形差分」もあわせて参照してよい。

- **系統図・関係図型**：家系図・登記記録の名義人相互の関係など、当事者・要素の関係性を線でつなぐ図（例：代襲相続の家系図、区分建物と敷地権の対応関係）。

  **家系図を描く場合の注意（2026-09-14判明・再発防止）**：H30午後第3問（代襲相続）の作図ガイドで、親子・兄弟姉妹という関係の種類を区別せず、登場人物を機械的に1本の縦線に並べて矢印をすべて同じ向きに引いてしまう誤りが実際に発生した。家系図は続柄によって配置が変わるべきものであり、次を必ず守る。
  - **縦位置は世代を表す。** 親は子より上、祖父母は親より上に置く。ある肢だけ祖先（直系尊属）を扱う場合は、他の肢（直系卑属を扱う場合）とは上下の基準人物の位置が逆になってよい（例：直系卑属を問う肢は被相続人を最上段に、直系尊属を問う肢は被相続人を最下段に置く）。1つの記事内で肢ごとに向きが変わること自体は問題ではなく、その旨をパネル内に一言添えれば足りる。
  - **同じ世代の人物（兄弟姉妹等）は横に並べる。** 親子のように縦に重ねてはならない。共通の親を表す小さな分岐点（∩字型のブラケット線等）を介して2人を左右につなぐ。
  - **矢印は「相続権を失った人」から「その人の子」へ、実際の親子関係の向きに沿って引く。** 図全体を貫く1本の矢印ではなく、相続権を失った人とその子を結ぶ区間ごとに矢印と○×を配置し、被代襲者が複数世代連鎖する肢（再代襲の可否を問う肢等）では、区間ごとに判定が変わりうることを示す。
  - プロンプトの DIAGRAM-GUIDE REQUIREMENT 段落に、上記の「世代＝縦位置」「同世代＝横並び」「矢印は実際の続柄の向き」を明記し、各パネルの Diagram 本文でも机上の続柄（親子か兄弟姉妹か祖先か）に応じた配置を具体的に指定すること。

- **配置図型**：土地・建物・附属建物など、物理的な位置関係を描く図（例：甲建物と乙建物の接続の有無、管轄区域の境界）。
- **決定木（フローチャート）型**：複数の条件を順に判定して結論に至る肢に使う。ひし形の分岐ノードを用いる。
- **タイムライン型**：時系列で生じる出来事（死亡・登記・処分等の先後関係）を左右または上下の矢印で示す図。
- **対比枠型（別の話への切り分け）**：ある肢のわかりにくさが「条件を順に確認する」ことではなく、「そもそも異なる2つの制度・場面のどちらの話なのかを見分ける」ことにある場合に使う（例：意思表示の相手方に関するルールなのか、第三者との対抗関係に関するルールなのか）。左右または上下2枠に分け、それぞれの枠に該当する制度名・根拠条文・結論を対比させて描く。無理に1本の決定木に押し込めない。
- **正誤対比型（思い込みチェック型）**：多段階の条件判定ではなく、条文・制度の正確な文言を正しく覚えているかを問う肢（うっかり思い込みで誤読しやすい肢）に使う。「正しいルール」と「誤りやすい思い込み」を左右または上下で対比させ、誤っている側には×印や取り消し線を重ねて描く。

### 手順

1. 対象記事（`note-articles/{年度}-mondai/q{n}-*.md`）の②のインフォグラフィックプロンプト（既に作成済みであることが多い）と、各肢の本文解説・まとめを読む。
2. 各肢について、「読者が問題文からどんな図を描けば正誤にたどり着けるか」「その図にたどり着くまでに、どの条件をどの順番で確認するか」を書き出す。原則→例外のような多段階の判定がある肢は、確認する条件を番号付きで列挙する。
3. 上記「画像の型」から各肢に最適なものを選ぶ（肢ごとに型が異なってよい）。
4. 下記「プロンプト雛形（作図ガイド型）」に流し込み、各パネルに Badge・Heading・Diagram・着眼点コールアウト・結論タグの4要素を用意する。多段階の条件判定がある肢では、Diagram を決定木として具体的に記述する（上記「フローチャート式の考え方」1〜2を参照）。
5. 各パネルを書き終えたら、「法的正確性の担保」の3項目（特に要件の圧縮・隠れた条件・本文との対応関係）を満たしているか、対象記事の本文解説・まとめを読み返して確認する。
6. 文字化け・簡体字対策・背景の不透明化（②の章を参照。CRITICAL TEXT REQUIREMENT・BACKGROUND REQUIREMENT・Final checkの三点を必ず含める。簡体字注意文は独立した日本語の一文にせず、必ずFinal checkの英文段落に埋め込む）を適用する。英文プロンプト本文内の括弧は半角`()`で統一し、全角`（`で開いて半角`)`で閉じる、またはその逆のような開閉の不一致がないか確認する。
7. 記事ファイルの末尾（既存の②インフォグラフィックプロンプトの後）に `## インフォグラフィック プロンプト（作図ガイド）` の見出しを立てて追記する。既存の②のセクションは変更しない。**見出し・Subtitleに肢の範囲（「ア〜オ」「1〜5」等）を書かない（重要・厳守、2026-09-25追加・25訂正）**：見出しは常に `（作図ガイド）` のみとし、「ア〜オ」はもちろん「1〜5」のような数字の範囲表記も付け足さない（文字数を増やさないため）。Subtitleも同様に範囲表記を含めず `{年度・問題番号} 作図ガイド（{分野の一言}）` の形にする。一方、`--- PANEL {N}（肢{記号}） ---` の`{記号}`部分（パネル1枚ごとの個別の識別表示。範囲表記ではない）は、この禁止の対象外であり、対象記事の問題文・本文解説・まとめが実際に使っている表記（「ア」「イ」…の記号を使う問題なら肢ア・肢イ…、「1」「2」…の数字を使う問題なら肢1・肢2…）にそのまま合わせる。⑤のパネル表記だけを記事本文と異なる独自の記号・番号に置き換えない。既存記事に見出し・Subtitleの範囲表記が残っている場合は、発見しだい削除する。
8. 画像は生成しない。記事ファイルにプロンプト文を追記して保存するところまでが成果物。保存前に、コードフェンス数が偶数であること・フェンス外に不要な半角括弧が残っていないこと・Markdown表（`|`で始まる行）が紛れ込んでいないことを機械的に確認する。

### プロンプト雛形（作図ガイド型）

```
Create a Japanese-language infographic, portrait layout, 1080x2600 pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, beige, gray), rounded panel sections, consistent with the
same visual language as the whole-problem poster for this article, but
built as a set of {N} diagram-drawing panels (a "how to sketch this fact
pattern, in the right order" study reference) rather than a
quick-reference conclusion poster.

DIAGRAM-GUIDE REQUIREMENT (critical): Each panel's purpose is to show the
reader exactly what diagram they should draw on scratch paper while
reading this type of problem, AND the order in which they should check
conditions to get there — {対象分野に応じたアイコン・要素を具体的に列挙}.
Where a 肢 requires checking multiple conditions in sequence before
reaching a conclusion, draw the panel's diagram as an actual decision
flowchart: diamond-shaped branch nodes with the condition written on
them, Yes/No (or ○/✕) branch arrows, and a final conclusion node. Where a
肢 is resolved by a single check, a labeled illustrative diagram is
sufficient — do not force a flowchart. Where a panel reuses a decision
tree shared with other panels in this set, render the branch relevant to
THIS panel with a thick highlighted border and full color, and render the
other, unrelated branches in a faded, greyed-out, or dotted-outline style
rather than omitting them — the reader should be able to see at a glance
which part of the shared tree this panel is about. Likewise, where a
diagram must show an entity that conceptually never held the right or
status in question (e.g. someone who was never an heir, or a claim that
never existed), render that entity or claim in a faded or dotted-outline
style rather than a plain ○/✕ mark, so the visual itself communicates
"this was never really there," not just "this is wrong." Unlike a
glanceable summary poster, each panel MAY include a short「着眼点」callout
box with 1-2 sentences that state the checking ORDER in words (e.g. "まず
〜を確認し、次に〜を確認します"), not just the conclusion. Do not include
case or precedent numbers (article/regulation numbers are fine); keep the
callout text as written below verbatim, and keep every condition each
callout describes faithful to the article's own body text — do not drop
or merge a required element (e.g. keep "善意" and "無過失" as two distinct
checks if the source article treats them as two distinct requirements).

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only — hiragana, katakana, and Jōyō (regular Japanese) kanji. Do NOT use
Simplified Chinese characters (simplified hanzi) under any circumstances,
even if a character looks similar. Do NOT use Traditional Chinese
characters (traditional hanzi) either, even where a traditional-hanzi
glyph looks close to the correct Japanese kanji form — every glyph must
match the standard Japanese Jōyō form exactly, not the Chinese
traditional variant. Do NOT render any character that is not standard
Japanese hiragana, katakana, or Jōyō kanji anywhere in the image —
no Chinese-only characters, no Korean Hangul, no other non-Japanese
script, and no stray or decorative glyphs of any kind, even as small
background or texture elements. Reproduce the exact text strings given
below verbatim — do not paraphrase, translate, summarize, or substitute
any characters. Within this English prompt text, use half-width
parentheses ( ) consistently — never open a parenthetical with a
full-width （ and close it with a half-width ), or vice versa.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances, even if the output file format
supports transparency. Fill the full canvas — including every corner and
margin outside the panels — with a solid or illustrated opaque background
(the pale beige/gray tone used elsewhere in this style is a good
default). There must be no checkerboard pattern, no partially transparent
area, and no unpainted canvas edge anywhere in the final image.

--- HEADER ---
Title (large, bold, 2行):
問題文を読んだら
どんな図を描けばいいか

Subtitle (smaller, centered, 1行):
{年度・問題番号} 作図ガイド（{分野の一言}）

（タイトル・サブタイトルのすぐ下にパネル群を続ける。導入イラスト・導入文の
ブロックは置かない。）

--- PANEL {N}（肢{記号}） ---
Badge: a filled circle in {COLOR} containing the number {N} (numbers run
continuously through all panels).
Heading (bold, ONE line):
{その肢で最初に何をすべきかを表す短い見出し。「完結した1文＋と確認」の
ような不自然な体言止めにしない。また、主語・対象を省いた「〜かどうかは
結論を変えない」のような抽象的な言い回しにせず、その1行だけで具体的な
内容がわかる文にする（上記「Headingの自然な日本語チェック」参照）}
Diagram: {図の構図を具体的に記述。多段階判定の肢は決定木として、分岐
ノード・条件ラベル・Yes/No矢印・結論ノードを明記する}
着眼点 callout (1-2 sentences, verbatim, must state the checking order):
{「まず〜を確認し、次に〜を確認します」のように順序を明示した1〜2文}
Conclusion tag (a short colored banner/pill, {COLOR}, 5-15 Japanese
characters):
{短い結論の一言}

（…肢の数だけ繰り返し。バッジ番号は1から通しで振る。）

--- FOOTER ---
Small footnote text (bottom of panel, small font, verbatim):
{条文根拠の小さな注記。判例・先例番号は書かない}

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional
Chinese, paying special attention to {列挙する漢字}. If any character
renders as a Simplified or Traditional Chinese variant, redraw that
character in the correct Japanese form. Also scan the entire canvas for
any character that is not standard Japanese hiragana, katakana, or Jōyō
kanji — including any Chinese-only character, Korean Hangul, other
non-Japanese script, or stray decorative glyph — and remove or redraw it
so that only standard Japanese text appears anywhere in the image.
Confirm the panel count equals {N} exactly, badge numbers run 1-{N}
continuously, there is no intro illustration or paragraph block between
the header and the panels, that every multi-condition 肢 is drawn as an
actual flowchart with branch nodes (not a bare illustration with no
visible decision structure), that no 肢 with a genuinely hidden second
condition has been flattened into a single check, that each 着眼点 callout
states a checking order rather than only a conclusion and keeps every
required element from the source article distinct (no merged or dropped
requirements), that any panel sharing a decision tree with another panel
clearly distinguishes its own highlighted branch from the other, faded
branches, confirm nothing is rendered below the last panel's footnote
text (no summary recap panel, no trophy or medal icon, no re-listed ○/✕
grid of all 肢, and no additional text block of any kind), and confirm the
entire canvas, edge to edge, is filled with a fully opaque background
with no transparency or alpha channel anywhere.
```
