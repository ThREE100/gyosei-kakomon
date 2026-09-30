# 行政書士試験 合格のための「1問1図解」インフォグラフィック設計(検討結果)

2026-09-30。過去問集(TAC合格革命2026、取り込みメモは[`../kakomonshu-tac/README.md`](../kakomonshu-tac/README.md))を題材に、
1問(=一問一答の1肢)ごとに図解インフォグラフィックを作るための設計検討。画像生成はChatGPT(手動)で行い、
このリポジトリ・Claude Codeで作るのは**プロンプト文まで**。

参照元:[`chosashi-infographic-prompt-template.md`](./chosashi-infographic-prompt-template.md)(土地家屋調査士向けに確立した固定ルール)。

## 1. 結論(先に要点)

1. **単位**:1肢(一問一答の1問)=1枚。土地家屋調査士の②(5肢俯瞰ポスター)ではなく、①〜⑤のどれとも違う
   「**1肢1枚の学習カード**」型として新設する。
2. **サイズ**:縦長 **1024×1536px(2:3)**。ChatGPT(GPT Image)が標準で出せる縦長サイズで、1問分の情報量に合う。
   (調査士の②は1080×1920だが、5肢分を載せるための大きさ。1肢1枚では文字が小さくなりすぎず、余白も余らない2:3が向く。)
3. **合格に効く設計の核は「なぜ○か×か」と「ひっかけの型」を毎回同じ場所に見せること**。行政書士の択一式は、
   知識を問うというより「肢の中の1か所のすり替え」を見抜く試験なので、答え(○×)より**すり替えの型**を覚えさせる。
4. **優先順位**:原本のランクA(430件)のうち、出題履歴が3回以上ある116件から作る。次に、出題履歴2回以上のA(239件)、
   最後にB・Cへ。最初は**科目ごとに1〜2問の試作(計5〜6枚)**でChatGPTの出力品質を確認してから量産する。
5. **これまでのルールで変えるもの/変えないもの**は下表(§6)。文字化け対策・背景不透明・アウトロ禁止は**そのまま踏襲**。

## 2. 合格から逆算した要件

行政書士試験(300点満点)の合格基準は、①全体で180点以上、②法令等科目で122点以上、③一般知識等科目で24点以上
(足切りあり)。配点は、択一式(法令等40問×4点=160点+一般知識等14問×4点=56点=216点)、多肢選択式(8点×3=24点)、
記述式(20点×3=60点)で、**配点の7割強を占める択一式の得点が合否を分ける**。ここから、図解に求める要件を導く。

| 合格に必要なこと | 図解デザインへの落とし込み |
|---|---|
| 択一式で「妥当でない肢」を短時間で切る | ○×の結論を最上部に固定し、すり替えポイントを1行で見せる(答え探しを不要にする) |
| 似た制度の混同が最大の失点原因(例:取消し/撤回、審査請求/異議申立て、心裡留保/錯誤/詐欺) | 対比図を基本形にする。「誤解」と「正しい形」を左右に並べる |
| 数字・期間・人数の暗記(例:審査請求期間、議決に必要な定足数) | 数字は「数字表」型の図に集約し、数字を必ず大きく・別色で表示する |
| 判例の結論(憲法・行政法に多い) | 「事件のシーン→裁判所の結論」の1コマ図解にする(判例番号は書かない) |
| 復習の優先度を自分で決められる | ランク(A/B/C)と出題回数を毎回同じ位置のバッジで表示する |
| 誤った内容を覚えない(誤肢の暗記事故を避ける) | 誤りの肢は**正しい記述に直して**図解する(調査士ルール踏襲)。誤りそのものは「誤解」枠で取り消し線付きで小さく見せるだけ |

## 3. 1肢1枚カードのレイアウト(固定)

上から下へ、次の6ブロックを固定順で置く。毎回同じ位置に同じ種類の情報があることで、学習者が「どこを見ればよいか」を
覚え、1枚あたりの認知負荷を下げる。

| # | ブロック | 内容 | 文字量の上限 |
|---|---|---|---|
| 1 | ヘッダー帯 | 科目バッジ(科目色)・ランクバッジ(A/B/C)・出題回数バッジ・論点タイトル(1行) | タイトル20字前後 |
| 2 | 判定スタンプ | 大きな「○ 正しい」または「× 誤り」のスタンプ+理由の一言。**ヘッダー直下の目立つ位置** | 理由15字前後 |
| 3 | メイン図解(全体の約55%) | 論点に応じた図(§4)。○×・ラベル札は図の中に埋め込む | ラベルは各10字前後 |
| 4 | ひっかけ帯 | 「ひっかけの型」アイコン+型の名前+この肢での具体的な1行 | 1行(30字以内) |
| 5 | 解き方帯 | 本番でこの肢に出会ったとき、どこを見れば判定できるかの1行 | 1行(30字以内) |
| 6 | 根拠の注記 | 条文番号(小さく)。判例は事件名のみ可、**判例・先例の番号は書かない** | 1行 |

- **結論タグ**(調査士②の5〜15字の帯)は、ブロック4の右側または図解の直下に1つだけ置く。
- **アウトロ禁止**:ブロック6の下には何も描かない(サマリー・トロフィー・○×グリッド等を禁止)。
- **文字は最小限**:ChatGPT系の画像生成は、日本語の長文を正確に描けない。1枚あたりの日本語の文字列は
  **10〜12個以内、各20字前後まで**を目安にし、指定した文字列以外は描かせない。

### ひっかけの型(ブロック4のタグ。6種に固定)

行政書士の択一肢が「誤り」になるときのすり替え方は、次の6つにほぼ分類できる。1肢に主たる型を1つ割り当てる。
(型の割り当ては**プロンプト作成時にClaudeが肢を読んで判断**し、機械的には決められない。)

| 型(タグ名) | すり替えの内容 | 例 |
|---|---|---|
| 主語すり替え | 権利義務の主体・対象者を入れ替える | 憲法尊重擁護義務は国民も負う(→公務員ら) |
| 数字すり替え | 期間・人数・割合・金額を変える | 審査請求期間、議決の定足数 |
| 要件の過不足 | 「かつ/または」、善意・無過失などの要件を足す/引く | 善意のみで足りる(→善意無過失) |
| 例外の見落とし | 原則だけを述べ、ただし書き・例外を無視する | 原則は取消し可、ただし… |
| 結論の逆転 | 判例・条文の結論(可/不可、有効/無効)を逆にする | 有効(→無効) |
| 手続の混同 | 似た制度・手続・機関の取り違え | 取消し/撤回、審査請求/再調査の請求 |

## 4. メイン図解の「型」(行政書士向け7種)

土地家屋調査士の型(系統図・配置図・決定木・タイムライン・対比枠・正誤対比)を、行政書士の出題に合わせて読み替える。

| 型 | 向く肢 | 描くもの | 主な科目 |
|---|---|---|---|
| ①対比型(誤解 vs 正) | 似た制度・主語のすり替え | 左に「誤解」枠(取り消し線)、右に「正しい形」枠 | 全科目(最も基本) |
| ②当事者関係図型 | 権利関係・三者以上の登場人物 | A・B・Cなどの人物アイコンと矢印(売買・債権・処分の向き) | 民法、行政法(行政庁・相手方・第三者) |
| ③要件判定フロー型 | 複数要件を順に満たす必要がある肢 | ひし形の分岐、はい/いいえ、結論ノード(両側の行き先を必ず書く) | 行政法(処分性・原告適格)、民法、会社法 |
| ④時系列型 | 期間・時効・手続の先後 | 横向きの時間軸、起算点、期間のバー | 民法(時効・期間)、行政法(不服申立て期間) |
| ⑤数字早見表型 | 数字・割合・人数の暗記 | 数字を大きく強調した2〜4行の表 | 会社法、地方自治法、行政法 |
| ⑥階層・権限図型 | 機関・権限の分担 | 国会・内閣・裁判所、行政機関の組織図、権限の矢印 | 憲法(統治)、地方自治法、会社法 |
| ⑦判例シーン型 | 判例の結論を問う肢 | 事件の当事者を1コマのシーンで描き、裁判所の結論札を添える | 憲法(人権)、行政法 |

- 多段階の判定が必要に見える肢でも、本文解説を読み直して**単一チェックで済むなら③にしない**(逆も同様)。調査士の⑤と同じ考え方。
- ③で「はい」「いいえ」のどちらも意味を持つ分岐は、両側の行き先を明記し、**ループ矢印を禁止**する(調査士⑤の判明済み事故の再発防止)。

## 5. 見た目のルール(デザイン)

| 項目 | 決定 | 理由 |
|---|---|---|
| 画風 | 淡いパステルのフラットデザイン+アイソメトリックのアイコン | 調査士シリーズと統一。ChatGPTで安定して出せる |
| 科目色 | 憲法=青 / 行政法=紫 / 民法=オレンジ / 商法・会社法=茶(ゴールド) / 業務関連諸法令・情報通信=水色 / 基礎法学・一般知識=グレー | 緑と赤を科目色から外し、○×のスタンプ色(緑/赤)と衝突させない |
| ○×の色 | ○=緑のスタンプ、×=赤のスタンプ(全枚共通で固定) | 一目で正誤が分かる。色覚多様性に配慮し、必ず「○」「×」の形も併記(色だけに頼らない) |
| ランクバッジ | A=金、B=銀、C=銅の丸バッジ。中の文字は「A」「B」「C」 | 復習優先度の一目判別。ただし**バッジの中の英字A/B/Cは例外的に許可**(調査士ルールの「英字禁止」の例外。§7参照) |
| 出題履歴の表示 | 「出題3回」のように回数のみ大きく。年度は「平17・平29」と漢字表記(H17等の英字は使わない) | 英字・数字混じりのIDは描画ミスを起こしやすい |
| 背景 | 全面不透明(薄いベージュ/グレー) | 調査士ルールのBACKGROUND REQUIREMENTをそのまま踏襲 |
| 文字 | 太めのゴシック体。図解内ラベルは大きく、注記だけ小さく | ChatGPTの日本語描画の精度を上げるため、文字は大きく少なく |

### 描画ミスを避けるためにChatGPT側で守らせること(調査士の判明済み事故から)

- 簡体字・繁体字・日本語以外の文字の混入禁止(冒頭とFinal checkで二重に明記)。漢字の注意喚起は**英語の`Final check`段落の一部**にする
  (独立した日本語の注意文は、画像内に描かれる事故が実際に起きている)。
- 対比カードで、同じ箱に○と×を両方指示しない。誤解と正しい形で結論が逆極性になる肢では、
  「左右で反対のマークにする」という趣旨の一文を必ず添える。1〜2文字しか違わない2つの文字列を並べる場合は、
  「同一ではない」ことと違う文字を明記する。
- 最後のブロックの下に、サマリー・トロフィー・○×グリッドを描かせない。

## 6. 調査士ルールとの差分

| 項目 | 調査士(参照元) | 行政書士1肢1枚カード |
|---|---|---|
| 単位 | 1問=5肢=1枚(②)、または記事単位 | **1肢=1枚** |
| サイズ | 1080×1920 / 1080×2600 | **1024×1536** |
| 文字量 | ②は結論タグのみ(GLANCEABLE)、④⑤は制限なし | **中間**:ひっかけ帯・解き方帯に各1行まで許可。長文の条文引用は不可 |
| 誤肢の扱い | 正しいルールに直して図解 | 同じ(誤肢は「誤解」枠に小さく取り消し線で示すのみ) |
| ヘッダーの正誤結論 | サブタイトルに正誤を書かない(5肢の答えを隠すため) | **書く**(1肢1枚では判定スタンプが主役。復習用途のため) |
| 番号・ID | 出題年度・問題番号を半角括弧で付記 | 出題「回数」と年度の漢字表記(英字IDは使わない) |
| 判例 | 番号は書かない | 同じ(事件名のみ可) |
| 法令基準 | 現行法(記事の法改正メモ方式) | 現行法。本書の法令基準日は令和7年11月10日現在(令和8年4月1日施行予定を含む)。基準日以降の改正は要確認 |

## 7. 固定プロンプト雛形(1肢1枚カード)

`{...}`が肢ごとに埋めるスロット。ガード文(CRITICAL TEXT・BACKGROUND・Final check)は**削らない**。

```
Create a Japanese-language study-card infographic, portrait layout,
1024x1536 pixels, clean flat-design isometric illustration style with soft
pastel colors, rounded panel sections, one card that teaches exactly one
true/false statement from the Japanese administrative scrivener (gyosei
shoshi) exam. Accent color for this card: {SUBJECT_COLOR}.

CARD-LAYOUT REQUIREMENT (critical): Build the card from top to bottom in
exactly this order and do not add, remove, or reorder blocks: (1) header
band, (2) verdict stamp, (3) main diagram, (4) trap band, (5) solving-tip
band, (6) small source note. This is a quick-reference study card, NOT a
text-heavy explainer: do not render any paragraph of prose. Every text
string on the card is one of the strings written below, verbatim, and no
other text may appear anywhere.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only - hiragana, katakana, and Joyo (regular Japanese) kanji, plus Arabic
numerals, plus the single letters A, B, or C inside the rank badge only.
Do NOT use Simplified Chinese characters under any circumstances, even if
a character looks similar. Do NOT use Traditional Chinese characters
either, even where a traditional glyph looks close to the correct Japanese
kanji form - every glyph must match the standard Japanese Joyo form
exactly. Do NOT render any other Latin letters, Korean Hangul, other
non-Japanese script, or stray or decorative glyphs of any kind, even as
small background or texture elements. Reproduce the exact text strings
given below verbatim - do not paraphrase, translate, summarize, or
substitute any characters. Within this English prompt text, use half-width
parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances. Fill the full canvas, including every
corner and margin outside the panels, with a solid or illustrated opaque
pale beige/gray background. There must be no checkerboard pattern, no
partially transparent area, and no unpainted canvas edge anywhere.

--- BLOCK 1: HEADER BAND ---
Subject badge (pill, {SUBJECT_COLOR}): {SUBJECT}
Rank badge (round {RANK_METAL} medal with the letter {RANK} inside): {RANK}
Frequency badge (small pill): 出題{N}回
Title (large, bold, ONE line):
{TITLE}

--- BLOCK 2: VERDICT STAMP ---
A large round stamp, {VERDICT_COLOR}, containing the single symbol {VERDICT_MARK}
and the label {VERDICT_LABEL}. Next to it, one short reason (verbatim):
{REASON}

--- BLOCK 3: MAIN DIAGRAM ({DIAGRAM_TYPE}) ---
{DIAGRAM_DESCRIPTION: concrete layout, icons, arrows, and every label string
verbatim. If two boxes contrast a mistaken belief and the correct rule, put
exactly ONE mark in each box, never both a check and a cross in the same
box. Where the two sides must show OPPOSITE marks, say so explicitly.}

--- BLOCK 4: TRAP BAND ---
Small tag icon with the trap-type label (verbatim): {TRAP_TYPE}
One line (verbatim): {TRAP_LINE}

--- BLOCK 5: SOLVING-TIP BAND ---
One line (verbatim): {TIP_LINE}

--- BLOCK 6: SOURCE NOTE ---
Small footnote text, bottom of the card, verbatim:
{SOURCE}

Final check before rendering: scan every kanji glyph, paying special
attention to {KANJI_WATCH_LIST}, and confirm each is in standard Japanese
(Joyo) form, not Simplified Chinese and not Traditional Chinese. If any
character renders as a Simplified or Traditional Chinese variant, redraw
it in the correct Japanese form. Scan the entire canvas for any character
that is not standard Japanese text (or the rank letter) and remove or
redraw it. Confirm there are exactly six blocks in the specified order,
that every text string matches the strings above verbatim, that no
paragraph of prose appears, that the verdict stamp matches {VERDICT_MARK},
that any two contrasted boxes carry different marks as specified,
that nothing is rendered below the source note (no summary recap panel, no
trophy or medal icon apart from the rank badge, no re-listed check/cross
grid, and no additional text block of any kind), and confirm the entire
canvas, edge to edge, is filled with a fully opaque background with no
transparency or alpha channel anywhere.
```

**スロット作成時のチェックリスト**(調査士ルールから継承):

1. TITLE・REASON等を確定したら、それ以上言い換えない。
2. KANJI_WATCH_LISTは、そのプロンプト本文に**実際に登場する**誤りやすい漢字だけを挙げ、grepで機械照合する。
3. 誤りの肢は、DIAGRAM_DESCRIPTIONで**正しい形**を主役に描き、誤解は左(または上)の小さな枠に取り消し線で示す。
4. 法的内容は、`data/oneliner.json`・条文(`laws/`)・本文解説と照合し、自分の言葉で書く。原本(書籍)の解説文は転記しない。

## 8. 試作プロンプト(サンプル1枚:憲法99条)

`data/oneliner.json` id=1(原本ランクB、出題履歴2回:平成17年度・平成29年度)を題材にした試作。設計の確認用であり、
ChatGPTで画像化して品質を確かめるための見本。

```
Create a Japanese-language study-card infographic, portrait layout,
1024x1536 pixels, clean flat-design isometric illustration style with soft
pastel colors, rounded panel sections, one card that teaches exactly one
true/false statement from the Japanese administrative scrivener (gyosei
shoshi) exam. Accent color for this card: blue.

CARD-LAYOUT REQUIREMENT (critical): Build the card from top to bottom in
exactly this order and do not add, remove, or reorder blocks: (1) header
band, (2) verdict stamp, (3) main diagram, (4) trap band, (5) solving-tip
band, (6) small source note. This is a quick-reference study card, NOT a
text-heavy explainer: do not render any paragraph of prose. Every text
string on the card is one of the strings written below, verbatim, and no
other text may appear anywhere.

CRITICAL TEXT REQUIREMENT: All text must be rendered in standard Japanese
only - hiragana, katakana, and Joyo (regular Japanese) kanji, plus Arabic
numerals, plus the single letters A, B, or C inside the rank badge only.
Do NOT use Simplified Chinese characters under any circumstances, even if
a character looks similar. Do NOT use Traditional Chinese characters
either, even where a traditional glyph looks close to the correct Japanese
kanji form - every glyph must match the standard Japanese Joyo form
exactly. Do NOT render any other Latin letters, Korean Hangul, other
non-Japanese script, or stray or decorative glyphs of any kind, even as
small background or texture elements. Reproduce the exact text strings
given below verbatim - do not paraphrase, translate, summarize, or
substitute any characters. Within this English prompt text, use half-width
parentheses ( ) consistently.

BACKGROUND REQUIREMENT (critical): The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances. Fill the full canvas, including every
corner and margin outside the panels, with a solid or illustrated opaque
pale beige/gray background. There must be no checkerboard pattern, no
partially transparent area, and no unpainted canvas edge anywhere.

--- BLOCK 1: HEADER BAND ---
Subject badge (pill, blue): 憲法
Rank badge (round silver medal with the letter B inside): B
Frequency badge (small pill): 出題2回
Title (large, bold, ONE line):
憲法を守る義務は誰にある

--- BLOCK 2: VERDICT STAMP ---
A large round stamp, red, containing the single symbol ✕ and the label 誤り.
Next to it, one short reason (verbatim):
国民は義務の対象外

--- BLOCK 3: MAIN DIAGRAM (contrast: mistaken belief vs correct rule) ---
Two side-by-side rounded boxes of equal height with an arrow-shaped divider.
LEFT box (small, grey-blue header tag 誤解): an isometric icon of ordinary
citizens (a small group of people) with a single red ✕ drawn over it and a
name tag 国民. This box carries the red ✕ only and NO check mark.
RIGHT box (larger, blue header tag 正しい形): a large isometric icon of the
constitution book at the top, and below it a row of five small icons, each
with a short name tag directly under it, in this order: 天皇・摂政 (a crown
icon), 国務大臣 (a person at a desk), 国会議員 (a parliament building),
裁判官 (a gavel), その他の公務員 (a person with an ID badge). This box
carries one green ✓ mark only, placed beside the book icon, and NO red ✕.
IMPORTANT: the two boxes must show DIFFERENT marks - the left box a red ✕,
the right box a green ✓ - do not draw the same mark in both boxes.

--- BLOCK 4: TRAP BAND ---
Small tag icon with the trap-type label (verbatim): 主語すり替え
One line (verbatim): 義務を負う側に国民は入らない

--- BLOCK 5: SOLVING-TIP BAND ---
One line (verbatim): 誰が義務を負うのかを主語で確認

--- BLOCK 6: SOURCE NOTE ---
Small footnote text, bottom of the card, verbatim:
根拠:憲法第99条

Final check before rendering: scan every kanji glyph, paying special
attention to 憲, 護, 義, 務, 摂, 臣, 裁, and 判, and confirm each is in
standard Japanese (Joyo) form, not Simplified Chinese and not Traditional
Chinese. If any character renders as a Simplified or Traditional Chinese
variant, redraw it in the correct Japanese form. Scan the entire canvas for
any character that is not standard Japanese text (or the rank letter) and
remove or redraw it. Confirm there are exactly six blocks in the specified
order, that every text string matches the strings above verbatim, that no
paragraph of prose appears, that the verdict stamp shows ✕ and 誤り, that
the left and right boxes of the main diagram carry different marks (left
red ✕, right green ✓), that nothing is rendered below the source note (no
summary recap panel, no trophy or medal icon apart from the rank badge, no
re-listed check/cross grid, and no additional text block of any kind), and
confirm the entire canvas, edge to edge, is filled with a fully opaque
background with no transparency or alpha channel anywhere.
```

## 9. 量産の進め方(提案)

1. **試作(5〜6枚)**:憲法・行政法・民法・会社法から各1〜2問(§8のサンプルを含む)をChatGPTで画像化し、
   文字の崩れ・簡体字混入・レイアウト順・○×の描き分けを確認する。結果を受けて雛形を1回だけ改訂する。
2. **優先順位で量産**:ランクA+出題3回以上(116件)→ランクA+2回以上(239件まで)→ランクB→ランクC。
3. **保存形式**:`note-articles/infographic/prompts/{科目}/{通し番号}.md`(1ファイル1肢、コードブロックにプロンプトを記録)。
   1ファイルにまとめると差分確認が難しくなるため、科目ごとのディレクトリに分ける。
4. **各肢の作業フロー**:肢を確認(`data/oneliner.json`で肢の本文・正誤)→自分の言葉で論点を整理→ひっかけの型を判定→図の型を選ぶ→
   雛形に流し込む→§7のチェックリストで検証(漢字リストの機械照合を含む)→保存。
5. **作業ごとにコミット**(まとめて1コミットにしない)、完了したら`main`へPR・マージ(`CLAUDE.md`の保存先ルール)。

## 10. ユーザーに確認したい点

- **1肢1枚でよいか**:1,000枚以上になる規模。関連する肢(例:同じ条文の肢が5つ並ぶ)を1枚にまとめる案もある(1枚=1論点)。
  試作の結果を見て決めるのが確実。
- **本書の法令基準日**(令和7年11月10日)と、現行法の差異は、図解作成時に都度確認する(全件の事前確認はしない)。
- 多肢選択式・記述式(問44〜46等)の図解は、本書が一問一答形式のためこの設計の対象外。必要なら別途設計する。
- 非公開リポジトリを用意すれば、書籍のOCR全文もそこに保存できる(現状はこの環境から作成できない)。
