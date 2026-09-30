## 【行政書士受験生向け】平成30年度 第21問〜収用の補償は「誰が」「何を」「どう争うか」の3点セットで覚えるんです〜

**出題年度：平成30年度　第21問**

> 問題21　道路用地の収用に係る損失補償に関する次の記述のうち、正しいものはどれか。
>
> 1　土地を収用することによって土地所有者が受ける損失は、当該道路を設置する起業者に代わり、収用裁決を行った収用委員会が所属する都道府県がこれを補償しなければならない。
>
> 2　収用対象となる土地が当該道路に関する都市計画決定によって建築制限を受けている場合、当該土地の権利に対する補償の額は、近傍において同様の建築制限を受けている類地の取引価格を考慮して算定した価格に物価変動に応ずる修正率を乗じて得た額となる。
>
> 3　収用対象の土地で商店が営まれている場合、商店の建築物の移転に要する費用は補償の対象となるが、その移転に伴う営業上の損失は補償の対象とはならない。
>
> 4　収用対象とはなっていない土地について、隣地の収用によって必要となった盛土・切土に要する費用は損失補償の対象になるが、それにより通路・溝等の工作物が必要となったときは、当該工作物の新築に係る費用は補償の対象とはならない。
>
> 5　収用対象の土地の所有者が収用委員会による裁決について不服を有する場合であって、不服の内容が損失の補償に関するものであるときは、土地所有者が提起すべき訴訟は当事者訴訟になる。

土地収用法は、公共事業のために土地を強制的に取得する「収用」の手続と、そのとき所有者などが受ける損失の補償のしくみを定めた法律です。本問は、道路用地の収用を題材に、①補償をする人は誰か、②補償額はどう算定されるか、③どこまでの損失が補償の対象か、④補償の額に不満があるときはどんな訴訟を起こすか、という4つの視点から、5つの記述の正誤を問うています。解説の条文は、本リポジトリに保存した現行の土地収用法（`laws/tochishuuyouhou.md`）の条文で確認しています。肢2に出てくる「建築制限を織り込まずに算定する」という考え方だけは、条文ではなく最高裁の判例の理解によるもので、その部分は末尾の確認事項に書いています。

### 1：損失を補償するのは収用委員会の所属する都道府県なのか

土地収用法68条は、「土地を収用し、又は使用することに因つて土地所有者及び関係人が受ける損失は、起業者が補償しなければならない」と定めています。補償をする義務を負うのは、事業を行う側である「起業者」（道路であれば、道路をつくる国や自治体などの事業主体）です。収用委員会は、収用の裁決（権利を取得する時期や補償額などを決める判断）を行う第三者的な機関であり、補償を支払う立場ではありません。

**たとえば**、市が道路をつくるために土地を収用する場合、補償金を支払うのは事業主体である市です。収用委員会が置かれている都道府県が、市に代わって支払うわけではありません。

本肢は、起業者に代わって収用委員会が所属する都道府県が補償するとしており、誤りです。

### 2：建築制限を受けている土地の補償額は、制限を受けた類地の価格で決めるのか

収用する土地の補償額について、土地収用法71条は、「収用する土地又はその土地に関する所有権以外の権利に対する補償金の額は、近傍類地の取引価格等を考慮して算定した事業の認定の告示の時における相当な価格に、権利取得裁決の時までの物価の変動に応ずる修正率を乗じて得た額とする」と定めています。本肢の後半の「物価変動に応ずる修正率を乗じて得た額」という部分は、この規定と合っています。

問題は、建築制限の扱いです。71条の条文には、建築制限（都市計画による制限）を受けていることをどう扱うかは書かれていません。この点は、最高裁が、道路整備のために都市計画で建築制限がかけられた土地について、その制限を受けていない状態を前提にして価格を算定するべきだという考え方を示していると理解されています（判決原文は未確認です）。事業のために課された制限のせいで補償額が低くなってしまうのは公平ではない、という発想です。本肢のように、「同様の建築制限を受けている類地の取引価格」を基準にすると、制限を織り込んだ低い価格になってしまうため、誤りと整理されます。

**ここが分かりにくいポイント**：
「近傍類地の取引価格」と書いてあるので、「同じ条件の類地を見ればよい」と読みたくなります。ここは、2段階で考えます。まず、収用する土地の価格を「その土地が事業の制限を受けていないとしたらいくらか」という基準で見ます。次に、その価格を決めるための参考として、近傍の類地の取引価格を使います。つまり、制限の有無は、参考にする類地の条件ではなく、評価の前提条件として決まります。

### 3：営業上の損失は補償の対象にならないのか

土地収用法77条は、収用する土地に物件（商店の建築物など）があるときは、「その物件の移転料を補償して、これを移転させなければならない」と定めています。建築物の移転に要する費用は、ここで補償されます。

これとは別に、88条は、71条・72条・74条・75条・77条・80条・80条の2に規定する損失の補償のほか、「離作料、営業上の損失、建物の移転による賃貸料の損失その他土地を収用し、又は使用することに因つて土地所有者又は関係人が通常受ける損失は、補償しなければならない」と定めています。「営業上の損失」は、条文自身が「通常受ける損失」の例として挙げています。商店が収用の対象になったことで、店を移転する間の営業ができなくなる損失は、その典型例です。

したがって、建築物の移転費用だけでなく、移転に伴う営業上の損失も補償の対象になります。本肢は、営業上の損失は補償の対象にならないとしており、誤りです。

### 4：隣地の収用で必要になった工作物の新築費は補償されないのか

肢4は、「収用対象とはなっていない土地」について、隣地の収用により必要となった工事の費用の補償を問うています。これに当たる規定は、土地収用法93条1項です。同項は、土地を収用し、その土地を事業の用に供することにより、「当該土地及び残地以外の土地について、通路、溝、垣、さくその他の工作物を新築し、改築し、増築し、若しくは修繕し、又は盛土若しくは切土をする必要があると認められるときは、起業者は、これらの工事をすることを必要とする者の請求により、これに要する費用の全部又は一部を補償しなければならない」と定めています。

つまり、条文は、盛土・切土と、通路・溝・垣・さくなどの工作物の新築・改築・増築・修繕とを、同じ文の中で並べて、どちらも費用補償の対象としています。盛土・切土の費用は補償されるが工作物の新築費は補償されない、という区別は条文にありません。

**ここが分かりにくいポイント**：
似た規定として、75条があります。75条は、同一の土地所有者に属する一団の土地の一部を収用することで、「残地」に工作物の新築等や盛土・切土をする必要が生じたときの費用を補償する規定です。つまり、75条は残地（収用されずに残った自分の土地）、93条は残地以外の土地（収用の対象でもなく、残地でもない土地）が対象です。本肢は「収用対象とはなっていない土地」の「隣地」の収用によるものですから、まず93条の場面かどうかを確認します。ただし、75条も93条も、盛土・切土と工作物の新築等を並べて補償の対象にしている点は同じなので、どちらの条文で考えても、本肢の「工作物の新築費は補償されない」は誤りです。

本肢は、工作物の新築に係る費用は補償の対象とならないとしており、誤りです。

### 5：補償の額に不服があるとき、土地所有者が起こす訴訟は当事者訴訟か

収用委員会の裁決のうち、損失の補償だけに不満がある場合は、裁決そのものを取り消してもらうのではなく、補償の額を争う訴訟を起こします。土地収用法133条は、収用委員会の裁決に関する訴えのうち損失の補償に関する訴えについて、2項で「裁決書の正本の送達を受けた日から六月以内に提起しなければならない」と定め、3項で、この訴えは、これを提起した者が起業者であるときは土地所有者又は関係人を、土地所有者又は関係人であるときは起業者を、「それぞれ被告としなければならない」と定めています。つまり、土地所有者が原告なら起業者が、起業者が原告なら土地所有者・関係人が被告になり、収用委員会は被告になりません。なお、補償以外の裁決の違法を争う訴えの出訴期間は、133条1項により三月です。

行政事件訴訟法4条は、当事者訴訟を「当事者間の法律関係を確認し又は形成する処分又は裁決に関する訴訟で法令の規定によりその法律関係の当事者の一方を被告とするもの及び公法上の法律関係に関する確認の訴えその他の公法上の法律関係に関する訴訟」と定義しています（本リポジトリの法令ファイルで確認済み）。補償の額を争うこの訴訟は、処分（収用裁決）に関する訴訟ですが、処分の効力を争うのではなく、法令（133条3項）の規定によって法律関係（補償の額）の当事者の一方を被告とするものなので、当事者訴訟の中でも「形式的当事者訴訟」と呼ばれる類型に当たります。

**ここが分かりにくいポイント**：
収用委員会の裁決という「行政庁の処分」に不服があるのだから、処分の取消訴訟だろう、と考えるのが自然です。ここは、2段階で確認します。まず、不服の内容が、収用そのもの（収用が適法か）なのか、補償の額だけなのかを見分けます。次に、補償の額だけの不服であれば、収用委員会ではなく、補償をめぐる当事者（起業者または土地所有者・関係人）を被告とする当事者訴訟（形式的当事者訴訟）になります。

本肢は、この整理のとおりで、正しい記述です。

### まとめ

- **1（誤）** 補償をするのは、事業を行う起業者であり（68条）、収用委員会が所属する都道府県ではない
- **2（誤）** 建築制限を受けている土地でも、制限を受けていない状態を前提に算定するべきで、制限を受けた類地の価格で算定するわけではない
- **3（誤）** 建築物の移転費用（77条）のほか、営業上の損失も「通常受ける損失」として補償の対象になる（88条）
- **4（誤）** 収用する土地・残地以外の土地でも、盛土・切土の費用に加え、通路・溝等の工作物の新築費も補償の対象になる（93条1項）
- **5（正）** 補償の額に関する不服は、起業者と土地所有者・関係人を当事者とする当事者訴訟（形式的当事者訴訟）で争う（133条2項・3項）

損失補償の問題は、「誰が払うか」「何が対象か」「どこまで補償するか」「どう争うか」を1つずつ切り分けて整理すると、選択肢を機械的に消せるようになります。

**正解：選択肢5番**

---

**法改正メモ（出題当時と現行法の差）**

- 法令基準日：本文の解説は2026年9月時点で施行されている法令に基づく。
- 出題当時の公式正解：選択肢5番（平成30年度の法令に基づく）。
- 差異のある肢・条文：肢1（土地収用法68条）、肢2（71条）、肢3（77条・88条）、肢4（93条1項、75条）、肢5（133条）を現行条文（令和8年6月24日施行時点）で確認した結果、出題当時と現行法で、結論に影響する差異は確認されなかった（確認範囲：上記の現行条文と、行政事件訴訟法4条。平成30年度当時の条文との対照は未実施）。結論への影響：なし。
- 現行法で解いた場合の結論：出題当時と同じ（選択肢5番が正しい）。
- 出題当時の条文の確認経路：`laws/tochishuuyouhou.md`は現行法のため、平成30年度当時の条文はローカルでは照合不可。当時と同じ規定内容であるとの理解は一般的な理解によるもので、新旧対照表・改正法では未確認（特に、同ファイルの冒頭に記された令和8年法律第46号による改正が本問の条文に及ぶかどうかも未確認）。建築制限に関する最高裁の考え方は判例未照合。

**このまま使える点／使う前に確認したい点**

- 出題番号・正解番号は、公式PDF本文および著者提供の公式正解表で確認済み（data/exam.jsonにH30は未収録）。
- 行政事件訴訟法4条の当事者訴訟の定義は、著者提供のe-Gov法令検索HTMLエクスポート（`note-articles/laws/gyosei-jiken-soshouhou.md`、令和8年5月21日施行時点）で直接確認しました。
- 土地収用法の条文（68条、71条、75条、77条、88条、93条、133条）は、著者提供のe-Gov法令検索のテキスト（`note-articles/laws/tochishuuyouhou.md`、令和8年6月24日施行時点）で直接確認しました。逐語引用は、同ファイルの条文（歴史的仮名遣いを含む）と照合しています。肢2の「建築制限を受けていない状態を前提に算定する」という最高裁の考え方は、71条の条文にはなく、判決原文を確認できていない著者の知識にもとづく整理であり（判例未照合）、確認が弱い部分です。肢2は、この点が弱いため、結論を公式正解（5）との整合でも支えています。
- 重複出題チェック（2026-09-30実施）：`data/exam.json`（令和2〜7年度）を、論点キーワード（損失補償、収用、土地収用法）と問題文冒頭「道路用地の収用」の両方で横断検索した。本問と同一の択一問題は見当たらない。令和6年度第42問（多肢選択式）は、土地収用法88条の「通常受ける損失」の解釈（輪中堤の文化財的価値は補償の対象にならない）を扱い、本問の肢3（営業上の損失も補償対象）と同じ88条に関わるが、論点は異なり、結論に矛盾はない。令和4年度第43問（多肢選択式）は国家補償の谷間を扱う別の問題である。

---

## 見出し画像用フレーズ

- 収用の補償を払うのは、収用委員会の都道府県じゃないんです
- 建築制限は、補償額を下げる理由にならないんです
- 営業上の損失も、「通常受ける損失」として補償されます
- 工作物の新築費も、工事費用の補償の対象なんです
- 補償の額の争いは、当事者訴訟になるんです

---

## インフォグラフィック プロンプト（問題全体）

1〜5の5つの記述を、「何を誰が補償するか（1〜4）」と「裁決への不服の争い方（5）」の2系統に整理し、誤りの肢（1〜4）は本来正しいルールに直した5枚のカードで1枚に俯瞰する構成。

```
Create a Japanese-language infographic, portrait layout, 1080x1920 pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, beige, gray), rounded card sections, consistent with a
modern explainer-graphic aesthetic (icons: isometric road under construction, survey flags, coin bags, document folders, courthouse, scales of justice, small shop building, stamp seals — adapt icon set to the topic).

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
summarize, or substitute any characters. Pay special attention to the
kanji 収・補・償・起・業・制・限・営・損・訴, which have visually
similar but structurally different Simplified/Traditional Chinese
counterparts — always draw the standard Japanese (Jōyō) form.

BACKGROUND REQUIREMENT (critical): 画像の背景は不透明にしてください。透過するデザインは禁止です。
The entire canvas must be fully opaque
from edge to edge. Do NOT generate a transparent or alpha-channel
background under any circumstances, even if the output file format
supports transparency. Fill the full canvas — including every corner and
margin outside the cards/columns — with a solid or illustrated opaque
background (the pale beige/gray tone used elsewhere in this style is a
good default). There must be no checkerboard pattern, no partially
transparent area, and no unpainted canvas edge anywhere in the final
image.

--- HEADER ---
Title (large, bold, 2行):
収用の補償の落とし穴
誰が・何を・どう争うかを切り分ける

Subtitle (smaller, centered, 1行):
平成30年度 第21問　道路用地の収用と損失補償

（タイトル・サブタイトルのすぐ下にカード群を続ける。導入イラスト・導入文の
ブロックは置かない。）

--- COLUMN A HEADER (pill-shaped badge, color: green) ---
何を誰が補償するか

--- COLUMN A, CARD 1 ---
Badge: a filled green circle containing the number 1.
Heading (bold, ONE line, ~20 characters or fewer):
補償するのは起業者
Illustration: An isometric road construction company building with a coin bag labeled「補償金」handing it to a landowner figure. A faded crossed-out prefecture building labeled「都道府県」with a red × mark.
Conclusion tag (green banner below the illustration, 5-15 characters):
起業者が補償する

--- COLUMN A, CARD 2 ---
Badge: a filled green circle containing the number 2.
Heading (bold, ONE line, ~20 characters or fewer):
建築制限を織り込まずに算定
Illustration: An isometric plot of land with a faded fence labeled「建築制限」lifted away, and a price tag labeled「制限がない状態の価格」. A faded crossed-out price tag labeled「制限を受けた類地の価格」with a red × mark.
Conclusion tag (green banner below the illustration, 5-15 characters):
制限がない前提で算定

--- COLUMN A, CARD 3 ---
Badge: a filled green circle containing the number 3.
Heading (bold, ONE line, ~20 characters or fewer):
営業上の損失も補償される
Illustration: An isometric small shop building with a moving truck, a coin bag labeled「移転費用」and a second coin bag labeled「営業上の損失」, both with checkmarks.
Conclusion tag (green banner below the illustration, 5-15 characters):
通常受ける損失を補償

--- COLUMN A, CARD 4 ---
Badge: a filled green circle containing the number 4.
Heading (bold, ONE line, ~20 characters or fewer):
工作物の新築費も補償される
Illustration: An isometric road cut with a slope of soil labeled「盛土・切土」and a ditch with a fence labeled「溝・垣・さく」, both with coin bag icons and checkmarks.
Conclusion tag (green banner below the illustration, 5-15 characters):
工事費用を補償

--- COLUMN B HEADER (pill-shaped badge, color: blue) ---
裁決への不服

--- COLUMN B, CARD 5 ---
Badge: a filled blue circle containing the number 5.
Heading (bold, ONE line, ~20 characters or fewer):
補償の額の争いは当事者訴訟
Illustration: An isometric courthouse with two figures facing each other across a table labeled「起業者」and「土地所有者」, a coin bag labeled「補償の額」between them. A faded committee building labeled「収用委員会」with a red × mark, showing it is not the defendant.
Conclusion tag (blue banner below the illustration, 5-15 characters):
当事者訴訟で争う

--- FOOTER ---

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional
Chinese, especially 収・補・償・起・業・制・限・営・損・訴. If any
character renders as a Simplified or Traditional Chinese variant, redraw
that character in the correct Japanese form. Also scan the entire canvas
for any character that is not standard Japanese hiragana, katakana, or
Jōyō kanji — including any Chinese-only character, Korean Hangul, other
non-Japanese script, or stray decorative glyph — and remove or redraw it
so that only standard Japanese text appears anywhere in the image. Confirm
the number of cards equals 5 exactly, with no duplicated or missing cards,
that badge numbers run 1-5 continuously across both columns without
resetting, confirm there is no intro illustration or paragraph block
between the header and the cards, confirm that no card contains a full
sentence of explanatory prose — every card's takeaway must read as a short
heading + a short conclusion tag, at a glance — confirm nothing is
rendered below the last card (no summary recap panel, no trophy or medal
icon, no re-listed ○/✕ grid of all 肢, and no additional text block of any
kind — the poster ends immediately after the last card), and confirm the
entire canvas, edge to edge, is filled with a fully opaque background with
no transparency or alpha channel anywhere.
```

---

## インフォグラフィック プロンプト（1〜5 作図ガイド）

問題文を読んだ瞬間に「何を確認し、どの順番で結論にたどり着くか」を、肢ごとに1パネルずつ示す解き方ガイド。肢5（不服の内容が収用そのものか補償の額だけか、誰を被告にするか）は複数の条件を順に確認するため、実際の決定木（フローチャート）として描く。②の俯瞰ポスターとは別物で、②の内容は書き換えない。

```
Create a Japanese-language infographic, portrait layout, 1080x2600 pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, beige, gray), rounded panel sections, consistent with the
same visual language as the whole-problem poster for this article
(収用の補償の落とし穴), but built as a set of 5 diagram-drawing panels (a
"how to sketch this fact pattern, in the right order" study reference)
rather than a quick-reference conclusion poster.

DIAGRAM-GUIDE REQUIREMENT (critical): Each panel's purpose is to show the
reader exactly what diagram they should draw on scratch paper while
reading this type of problem, AND the order in which they should check
conditions to get there — a road construction company handing a coin bag to a landowner, a plot of land with a lifted fence, a small shop with a moving truck, a road cut with a ditch and fence, and a courthouse with two parties across a table. Where a 肢 (or blank)
requires checking multiple conditions in sequence before reaching a
conclusion, draw the panel's diagram as an actual decision flowchart:
diamond-shaped branch nodes with the condition written on them, Yes/No
（はい／いいえ）branch arrows, and a final conclusion node. Where a 肢 is
resolved by a single check, a labeled illustrative diagram is sufficient —
do not force a flowchart. Unlike a glanceable summary poster, each panel
MAY include a short「着眼点」callout box with 1-2 sentences that state the
checking ORDER in words (e.g. "まず〜を確認し、次に〜を確認します"), not
just the conclusion. Do not include case or precedent numbers (article
numbers are fine); keep the callout text as written below verbatim, and
keep every condition each callout describes faithful to the article's own
body text — do not drop or merge a required element. Keep the two checks in Panel 5 (不服の内容は補償の額だけか and 被告は誰か) distinct.

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
any characters. Pay special attention to the kanji 収・補・償・起・業・制・限・営・損・訴, which have
visually similar but structurally different Simplified/Traditional Chinese
counterparts — always draw the standard Japanese (Jōyō) form. Within this
English prompt text, use half-width
parentheses ( ) consistently — never open a parenthetical with a
full-width （ and close it with a half-width ), or vice versa.

BACKGROUND REQUIREMENT (critical): 画像の背景は不透明にしてください。透過するデザインは禁止です。
The entire canvas must be fully opaque
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
平成30年度 第21問　作図ガイド（道路用地の収用と損失補償）

（タイトル・サブタイトルのすぐ下にパネル群を続ける。導入イラスト・導入文の
ブロックは置かない。）

--- PANEL 1（肢1） ---
Badge: a filled circle in green containing the number 1.
Heading (bold, ONE line):
補償する主体を確認する
Diagram: An isometric road construction company building labeled「起業者」with a coin bag labeled「補償金」handing it to a landowner figure, drawn with a thick highlighted border. Beside it, a faded grayed-out committee building labeled「収用委員会」and a faded prefecture building labeled「都道府県」, each with a red × mark.
着眼点 callout (1-2 sentences, verbatim, must state the checking order):
まず収用によって生じた損失を補償する義務を負うのは事業を行う起業者であることを確認し、次に裁決をする収用委員会や都道府県は補償する立場ではないことを確認します。
Conclusion tag (a short colored banner/pill, green, 5-15 Japanese
characters):
起業者が補償する

--- PANEL 2（肢2） ---
Badge: a filled circle in green containing the number 2.
Heading (bold, ONE line):
建築制限を前提にしないで算定する
Diagram: A contrast-frame diagram split into two isometric boxes. Left box labeled「正しい算定」shows a plot of land with a fence labeled「建築制限」lifted away and a price tag labeled「制限がない状態の価格」with a checkmark, plus a small label「物価変動の修正」. Right box labeled「誤りやすい算定」is faded, showing a price tag labeled「制限を受けた類地の価格」with a red × mark.
着眼点 callout (1-2 sentences, verbatim, must state the checking order):
まず収用する土地を建築制限を受けていない状態として評価することを確認し、次に事業の認定の告示の時の価格に物価変動の修正率を乗じることを確認します。
Conclusion tag (a short colored banner/pill, green, 5-15 Japanese
characters):
制限がない前提で算定

--- PANEL 3（肢3） ---
Badge: a filled circle in green containing the number 3.
Heading (bold, ONE line):
移転費用と営業上の損失を分けて確認する
Diagram: An isometric small shop building with a moving truck. Two coin bags side by side, the first labeled「移転費用」and the second labeled「営業上の損失」, both drawn with thick highlighted borders and checkmarks under a banner labeled「通常受ける損失」.
着眼点 callout (1-2 sentences, verbatim, must state the checking order):
まず建築物の移転に要する費用が補償されることを確認し、次に移転に伴う営業上の損失も通常受ける損失として補償されることを確認します。
Conclusion tag (a short colored banner/pill, green, 5-15 Japanese
characters):
通常受ける損失を補償

--- PANEL 4（肢4） ---
Badge: a filled circle in green containing the number 4.
Heading (bold, ONE line):
盛土・切土と工作物の両方を確認する
Diagram: An isometric road cut with a slope of soil labeled「盛土・切土」and a ditch with a fence labeled「溝・垣・さく」, each with a coin bag icon and a checkmark, under a banner labeled「工事費用の補償」.
着眼点 callout (1-2 sentences, verbatim, must state the checking order):
まず盛土や切土に要する費用が補償されることを確認し、次に通路や溝などの工作物の新築費用も補償されることを確認します。
Conclusion tag (a short colored banner/pill, green, 5-15 Japanese
characters):
工事費用を補償

--- PANEL 5（肢5） ---
Badge: a filled circle in blue containing the number 5.
Heading (bold, ONE line):
不服の内容と被告を順に確認する
Diagram: A decision-tree flowchart on an isometric courthouse scene. Start node (diamond): 不服の内容は補償の額だけか？ with a いいえ arrow to a conclusion node reading 裁決の取消訴訟など, and a はい arrow down to a second diamond node (thick highlighted border): 被告は起業者または土地所有者・関係人か？ with a はい arrow to a green checkmark conclusion node reading 当事者訴訟で争う, and a いいえ arrow (収用委員会を被告にする) to a red cross conclusion node reading 被告を誤っている.
着眼点 callout (1-2 sentences, verbatim, must state the checking order):
まず不服の内容が補償の額だけかを確認し、次に補償をめぐる当事者である起業者や土地所有者・関係人を被告とする訴訟になることを確認します。
Conclusion tag (a short colored banner/pill, blue, 5-15 Japanese
characters):
当事者訴訟で争う

--- FOOTER ---
Small footnote text (bottom of panel, small font, verbatim):
土地収用法68条・71条・77条・88条・93条・133条、行政事件訴訟法4条に基づく整理です。

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional
Chinese, paying special attention to
収・補・償・起・業・制・限・営・損・訴. If any character
renders as a Simplified or Traditional Chinese variant, redraw that
character in the correct Japanese form. Also scan the entire canvas for
any character that is not standard Japanese hiragana, katakana, or Jōyō
kanji — including any Chinese-only character, Korean Hangul, other
non-Japanese script, or stray decorative glyph — and remove or redraw it
so that only standard Japanese text appears anywhere in the image. Confirm
the panel count equals 5 exactly, badge numbers run 1-5 continuously,
there is no intro illustration or paragraph block between the header and
the panels, that Panel 5 (the only multi-condition choice) is drawn as an
actual flowchart with branch nodes (not a bare illustration with no
visible decision structure) and that both its はい and いいえ branches lead
to explicit conclusion nodes rather than a looping-back arrow, that each
着眼点 callout states a checking order rather than only a conclusion and
keeps every required element from the source article distinct (no merged
or dropped requirements), confirm nothing is rendered below the last
panel's footnote text (no summary recap panel, no trophy or medal icon,
no re-listed ○/✕ grid of all 肢, and no additional text block of any
kind), and confirm the entire canvas, edge to edge, is filled with a fully
opaque background with no transparency or alpha channel anywhere.
```
