## 【行政書士受験生向け】令和6年度 第34問〜実は全員が正解になった問題、それでも解き方は身につけておきたいんです〜

**出題年度：令和6年度　第34問**

> 不法行為に基づく損害賠償に関する次の記述のうち、民法の規定および判例に照らし、妥当なものはどれか。
>
> 1　不法行為による生命侵害の場合において、被害者の相続人であれば、常に近親者固有の慰謝料請求権が認められる。
>
> 2　法人が名誉毀損を受けた場合、法人には感情がないので、財産的損害を除き、非財産的損害の賠償は認められない。
>
> 3　交通事故による被害者が、いわゆる個人会社の唯一の代表取締役であり、被害者には当該会社の機関としての代替性がなく、被害者と当該会社とが経済的に一体をなす等の事情の下では、当該会社は、加害者に対し、被害者の負傷のため営業利益を逸失したことによる賠償を請求することができる。
>
> 4　不法行為により身体傷害を受けた被害者は、後遺症が残ったため、労働能力の全部又は一部の喪失により将来において取得すべき利益を喪失した場合には、その損害について定期金ではなく、一時金による一括賠償しか求めることができない。
>
> 5　交通事故の被害者が後遺症により労働能力の一部を喪失した場合に、その後に被害者が別原因で死亡したとしても、交通事故の時点で、その死亡の原因となる具体的事由が存在し、近い将来における死亡が客観的に予測されていたなどの特段の事情がない限り、死亡の事実は逸失利益に関する就労可能期間の認定において考慮されない。

不法行為に基づく損害賠償は、民法709条が定める「損害を賠償する責任を負う」という一言だけでは片付かず、「誰が請求できるのか」「どこまでの損害が対象になるのか」「どういう方法で支払うのか」という3つの局面で、条文の文言と判例の理解を積み重ねて答えを出す分野です。本問の1〜5は、この3局面（請求権者・損害の範囲・算定方法）を横断して問う内容になっています。

なお、本問は行政書士試験研究センターの公式発表により、選択肢1〜5のいずれを選んでも正解として採点された特殊な問題です（`data/exam.json`の`id="R6-34"`を実際に確認すると、`answer`フィールドが通常の数字ではなく`"all"`という文字列になっており、このデータセット全体の中でも唯一のケースです）。全員正解だからといって、各肢の解説を放棄するのではなく、通常どおり条文・判例の理解に基づいて「本来はどの記述が妥当と考えられるか」を1つずつ検討していきます。

### 1：近親者固有の慰謝料請求権が認められるのは父母・配偶者・子に限られる

不法行為によって被害者の生命が侵害された場合、被害者本人は死亡しているため、本人が損害賠償を請求することはできません。しかし、民法711条は、被害者本人の権利とは別に、近親者自身が独自に持つ請求権（近親者固有の慰謝料請求権）を認めています。「固有」というのは、被害者本人の請求権を近親者が相続して手にするのではなく、近親者自身がもともと持っている権利という意味です。

711条は次のように定めています。「他人の生命を侵害した者は、被害者の父母、配偶者及び子に対しては、その財産権が侵害されなかった場合においても、損害の賠償をしなければならない」。この条文が近親者固有の慰謝料請求権を認める対象は、「父母、配偶者及び子」という3種類の関係に明文で限定されています。

一方、「相続人」という言葉は、これとは別の広がりを持つ概念です。民法887条1項は「被相続人の子は、相続人となる」と定め、890条は「被相続人の配偶者は、常に相続人となる」と定めています。ここまでは711条の「父母、配偶者及び子」と重なりますが、889条1項は、被相続人に子がいない場合に、直系尊属（1号）や兄弟姉妹（2号）も順位に従って相続人となることを定めています。つまり、兄弟姉妹は、子がいない場合には相続人になり得ますが、711条が挙げる「父母、配偶者及び子」には含まれていません。

**たとえば**、Aが交通事故で死亡し、Aに子も配偶者もおらず、Aの兄Bだけが相続人になったとします。Bは889条1項2号により相続人にはなりますが、711条が明文で挙げているのは父母・配偶者・子であって兄弟姉妹ではないため、Bが711条に基づいて当然に近親者固有の慰謝料請求権を持つとまでは、条文の文言からは言えません。

**ここが分かりにくいポイント**：

「相続人になるくらい近い関係なら、慰謝料も認められて当然では」と感じるかもしれません。しかし711条は、相続人という広い概念全体に慰謝料請求権を認めているわけではなく、父母・配偶者・子という3種類の関係だけを名指しして特別に認めているにすぎません。相続人であることと、711条の請求権者であることは、重なる部分は多いものの、条文上は別のルールです。

本肢は、「被害者の相続人であれば、常に近親者固有の慰謝料請求権が認められる」としており、711条が父母・配偶者・子に限定して明文で認めているという条文の構造と一致しません。私自身の検討では、本肢は本来は妥当でない記述だと考えられます。

### 2：法人にも名誉権があり、無形の損害の賠償が認められる

不法行為による損害には、財産的損害（お金に換算しやすい損害）だけでなく、財産以外の損害も含まれます。民法710条は次のように定めています。「他人の身体、自由若しくは名誉を侵害した場合又は他人の財産権を侵害した場合のいずれであるかを問わず、前条の規定により損害賠償の責任を負う者は、財産以外の損害に対しても、その賠償をしなければならない」。この条文は、侵害された利益の一つとして「名誉」を明文で挙げ、名誉が侵害された場合には財産以外の損害についても賠償しなければならないと定めています。

ここでいう「名誉」とは、人が社会から受ける品性・信用等についての客観的な評価のことです（初学者向けに言えば、「あの人・あの会社は信頼できる」という周囲からの評価そのものです）。この評価は、自然人（個人）だけでなく、会社などの法人も社会的な信用として持っています。710条の「他人」を自然人に限定する文言はなく、法人も名誉を侵害され得る「他人」に含まれると理解されています。したがって、法人の名誉が毀損され、社会的信用が低下したような場合には、その無形の損害（財産的な損害とは別の、信用低下そのものの損害）についても、財産的損害と並んで賠償の対象になると考えられます。

**たとえば**、企業Cが虚偽の悪評を流されて取引先からの信用を失ったとします。取引が実際に減って生じた売上減少分は財産的損害ですが、それとは別に、社会的信用が低下したこと自体についても、Cは710条に基づいて賠償を求めることができると考えられます。

**ここが分かりにくいポイント**：

「感情がないなら、精神的な苦痛を賠償する慰謝料のような話は成り立たないのでは」と感じるかもしれません。しかし710条が保護しているのは、被害者の内面的な苦痛そのものではなく、社会から受ける客観的な評価（信用）です。法人は感情を持ちませんが、社会的な信用という客観的な評価は当然に持っており、その低下自体が無形の損害として賠償の対象になります。

本肢は、「法人には感情がないので、財産的損害を除き、非財産的損害の賠償は認められない」としており、710条が「名誉」を財産以外の損害の対象として明文で挙げていることと一致しません。私自身の検討では、本肢は本来は妥当でない記述だと考えられます。

### 3：経済的一体性等の特段の事情があれば、会社自身も営業損害の賠償を請求できる

民法709条は「故意又は過失によって他人の権利又は法律上保護される利益を侵害した者は、これによって生じた損害を賠償する責任を負う」と定めています。ここでの「他人」とは、原則として加害行為によって直接損害を受けた被害者本人を指します。したがって、交通事故で会社の代表取締役が負傷した場合、その代表者個人が709条に基づいて自分の損害（治療費・自分の給与の減少分など）を請求できるのが原則です。会社の営業利益が代表者の負傷によって間接的に減ったとしても、それは本来、代表者個人の負傷から生じた間接的な影響にすぎず、会社自身が709条の請求権者になるとは、通常はいえません。

しかし、いわゆる「個人会社」（実質的に1人の経営者が会社の資産・業務のすべてを握っているような会社）で、その代表者以外に会社の機関としての代替性がなく、代表者個人と会社とが経済的に一体をなしているといえるような特段の事情がある場合には、代表者の負傷と会社の営業利益の逸失との間に、通常の間接的な影響を超えた実質的なつながりがあると評価できます。このような特段の事情がある場合には、会社自身も、加害者に対して営業利益の逸失について直接賠償を請求できると考えられています。

**たとえば**、経営者D以外に実質的な業務執行者がいない会社Eにおいて、Dが交通事故で長期入院し、その間Eの営業がほとんど止まってしまったとします。Eには機関としてDを代替できる者がおらず、Eの資産・業務がDの活動と経済的に一体化しているといえる場合には、Eは加害者に対して、Dの負傷によって生じた営業利益の逸失について、自ら賠償を請求できると考えられます。

**ここが分かりにくいポイント**：

「損害を受けたのは代表者個人であって、会社は間接的に影響を受けただけでは」と感じるかもしれません。たしかにこれが原則ですが、個人会社のように会社と個人の経済的な実態が一体化している場合には、その一体性という特段の事情があることで、会社自身の損害と加害行為との結びつきを認めることができる、という例外的な考え方です。

本肢は、個人会社の唯一の代表取締役であり機関としての代替性がなく経済的に一体をなす等の事情の下で、会社が営業利益の逸失について賠償を請求できるとしており、この例外的な考え方と一致します。私自身の検討では、本肢は本来は妥当な記述だと考えられます。

### 4：将来の逸失利益は、一時金だけでなく定期金による賠償も求めることができる

不法行為により身体傷害を受け、後遺症が残った被害者は、労働能力の全部または一部を失うことで、将来得られたはずの利益を失います。これを逸失利益といいます（事故等がなければ将来得られたはずなのに、事故等によって失われてしまった利益のことです）。

損害賠償の方法について、民法722条1項は「第四百十七条及び第四百十七条の二の規定は、不法行為による損害賠償について準用する」と定めています。準用元の417条は「損害賠償は、別段の意思表示がないときは、金銭をもってその額を定める」と定め、賠償は原則として金銭で行うという原則（金銭賠償の原則）を示すにとどまります。417条の2は、将来の利益を現在の価値に換算する際の中間利息の控除方法を定めるものです。これらの条文は、賠償を金銭で行うことと、将来分を現在価値に置き換える計算方法を定めているだけで、その金銭を一括で支払うのか、定期的に分割して支払うのかという支払方法自体を一時金に限定する明文の規定にはなっていません。

このため、後遺障害による労働能力の喪失によって将来の利益を失った場合の逸失利益についても、当事者が一時金による一括賠償を求めることができるのはもちろんですが、それに加えて、将来にわたって定期的に支払う定期金による賠償を求めることも認められると考えられています。定期金賠償は、損害の発生状況（たとえば将来の稼働状況の変化）に応じた柔軟な算定を可能にする支払方法です。

**たとえば**、後遺障害により労働能力の一部を失った被害者Fが、将来の逸失利益について、事故直後にまとめて一括で受け取る一時金ではなく、毎年一定額を受け取る定期金の形で請求することも、民法上排除されていないと考えられます。

**ここが分かりにくいポイント**：

「損害賠償はまとめて一括で払うのが普通では」と感じるかもしれません。たしかに一時金による一括賠償が実務上多く用いられていますが、それは417条が定める金銭賠償の原則から当然に導かれる話であって、支払を一時金に限定する明文の規定があるわけではありません。定期金による賠償も選択肢として認められると理解されています。

本肢は、「その損害について定期金ではなく、一時金による一括賠償しか求めることができない」としており、支払方法を一時金に限定する明文の規定がないことと一致しません。私自身の検討では、本肢は本来は妥当でない記述だと考えられます。

### 5：死亡の事実は、原則として就労可能期間の認定に影響しない

逸失利益の算定は、被害者が将来にわたって働くことができたはずの期間（就労可能期間）を基礎として行われます。交通事故の時点で、被害者が将来どのくらいの期間働けたかを見積もり、それに基づいて将来の収入の見込みを算定するという構造です。

交通事故の被害者が後遺症により労働能力の一部を失った後、事故とは別の原因で死亡してしまった場合、この死亡の事実を就労可能期間の算定にどう反映させるかが問題になります。逸失利益の算定は、あくまで事故が発生した時点を基準として将来を見積もるものです。事故の後に生じた別原因による死亡という事情を、事後的に遡って就労可能期間の短縮に反映させてしまうと、被害者側にたまたま生じた事情によって賠償額が大きく左右されてしまい、不合理な結果になりかねません。そのため、交通事故の時点で、その死亡の原因となる具体的な事由が既に存在し、近い将来における死亡が客観的に予測されていたといった特段の事情がない限り、事後に生じた死亡の事実は、就労可能期間の認定において考慮されないと考えられています。

**たとえば**、交通事故で後遺障害を負ったGが、その後まったく無関係の病気で亡くなったとします。事故の時点でGにその病気の兆候がなく、近い将来の死亡が客観的に予測されるような事情もなかった場合には、Gの逸失利益の算定にあたっての就労可能期間は、事後の死亡の事実によって短縮されることなく、事故の時点での見積もりどおりに認定されると考えられます。

**ここが分かりにくいポイント**：

「結局死亡してしまったのだから、その時点で就労可能期間も終わりでは」と感じるかもしれません。しかし逸失利益の算定はあくまで事故時点を基準にした将来予測であり、事後に生じた別原因の死亡という偶然の事情まで反映させると、被害者側にとって不合理に不利な結果を招きます。特段の事情がある場合を除いて、死亡の事実は就労可能期間の認定に影響しないという考え方が採られています。

本肢は、特段の事情がない限り死亡の事実は就労可能期間の認定において考慮されないとしており、この考え方と一致します。私自身の検討では、本肢は本来は妥当な記述だと考えられます。

### まとめ

- **1（私見では本来は妥当でない）** 近親者固有の慰謝料請求権が認められるのは父母・配偶者・子に限られ、相続人であれば常に認められるわけではない（711条）
- **2（私見では本来は妥当でない）** 法人にも社会的信用という名誉があり、その毀損による無形の損害についても賠償が認められると考えられる（710条）
- **3（私見では本来は妥当）** 個人会社の唯一の代表者であり機関としての代替性がなく経済的に一体をなす等の特段の事情があれば、会社自身も営業利益の逸失について賠償を請求できると考えられる
- **4（私見では本来は妥当でない）** 将来の逸失利益は、一時金による一括賠償に限られず、定期金による賠償を求めることも認められると考えられる（722条1項・417条・417条の2）
- **5（私見では本来は妥当）** 死亡の事実は、特段の事情がない限り、就労可能期間の認定において考慮されないと考えられる

このように、条文・判例の一般的な理解に基づいて1つずつ検討すると、私自身の見解としては3と5の両方が「妥当なもの」として成立し得るように見えます。「妥当なものはどれか」という単一選択を求める形式でありながら、複数の記述が妥当と評価できる可能性がある点は、読者が自分で各肢を検討する際にも意識してよい着眼点です（なお、この点が全員正解とされた直接の理由であるかどうかは、後述のとおり確認できていません）。

**正解：本問は、行政書士試験研究センターの公式発表により、選択肢1〜5のいずれを選んでも正解として採点されました（`data/exam.json`の`answer`フィールドが`"all"`という特殊な値になっていることで確認済みです）。**

---

**このまま使える点／使う前に確認したい点**

- 出題番号・正解の特殊性は、`data/exam.json`の`id="R6-34"`を実際に確認して照合済み。`answer`フィールドが通常の数字ではなく文字列`"all"`になっていることを実際に確認した（このデータセット全体を通じて唯一のケースである）。問題文・選択肢1〜5の文言も同ファイルと完全に一致することを確認した。
- 各肢の法的根拠は、`note-articles/laws/minpou-2-saiken.md`（709条〈不法行為による損害賠償〉・710条〈財産以外の損害の賠償〉・711条〈近親者に対する損害の賠償〉・722条1項〈損害賠償の方法、中間利息の控除及び過失相殺〉・417条〈損害賠償の方法〉・417条の2〈中間利息の控除〉）を実際にgrepし、条文番号・項号・逐語引用を突き合わせて確認した。肢1で扱う相続人の範囲については、`note-articles/laws/minpou-3-shinzoku-souzoku.md`（887条1項〈子及びその代襲者等の相続権〉・889条1項1号及び2号〈直系尊属及び兄弟姉妹の相続権〉・890条〈配偶者の相続権〉）を実際にgrepして確認した。
- **全員正解とされた具体的な理由は一次資料未照合**：本問がなぜ選択肢1〜5のいずれを選んでも正解とされたのか、行政書士試験研究センターが公式に発表した具体的な理由（どの選択肢にどのような瑕疵があったため全員正解としたか）については、このリポジトリ内のどのファイルにも公式発表の原文が見当たらず、一次資料未照合である。まとめで述べた「私見では3と5の両方が妥当に見える」という指摘は、あくまで筆者自身の条文・判例の一般的な理解に基づく検討結果であり、公式に発表された理由そのものではない。
- **判例部分の一次資料未照合（B-7）**：肢2（法人の名誉権）・肢3（個人会社の代表者）・肢4（定期金賠償）・肢5（就労可能期間の認定）は、いずれも判例の一般的な理解に基づく論点である。このリポジトリには判例集の原文ファイルがなく、事件名・法廷名・年月日は一次資料未照合である。本文では判旨の結論・判断枠組みのみを述べ、断定的な事件情報は記載していない。
- 重複出題チェック（2026-09-25実施）：`data/exam.json`の全年度を横断検索した結果、問題文冒頭が完全に一致する他年度の出題は見当たらなかった。論点キーワード（「個人会社」「経済的一体」「就労可能期間」「代表取締役」「父母、配偶者及び子」等）による横断検索でも、本問（R6問34）以外の一致は見当たらなかった。「不法行為」を主題とする問題としてはR3問34（不法行為に関する記述のうち妥当でないものを選ぶ問題）が存在するが、その5肢は因果関係の立証・身体的特徴の斟酌・未成年者の過失相殺・名誉毀損の定義・医療水準というR6問34とは異なる論点を扱っており、本問が扱う711条の近親者固有の慰謝料請求権・法人の名誉毀損による無形の損害・個人会社の代表者・定期金賠償・就労可能期間の認定のいずれとも重複しない。R4問35（相続に関する記述）の肢2は、被害者本人の慰謝料請求権が相続財産に含まれるかという論点であり、これは本問の肢1が扱う近親者固有の慰謝料請求権（被害者本人の権利の相続ではなく、近親者自身の権利）とは別の論点であるため、重複出題としては扱わない。

---

## 見出し画像用フレーズ

- 実は全員正解になった問題、それでも解き方は身につけておきたいんです
- 相続人だからといって、慰謝料請求権が当然に認められるわけじゃないんです
- 法人だって、名誉を傷つけられたら泣き寝入りしなくていいんです
- 個人会社の社長が事故に遭ったら、会社自身も損害を訴えられるんです
- 逸失利益は、一括じゃなく分割で受け取る道もあるんです

---

## インフォグラフィック プロンプト（問題全体）

1〜5の5つの記述を、「誰が損害を請求できるか」（肢1〜3）と「損害をどう算定するか」（肢4・5）の2系統に整理し、本来正しいと考えられるルールに直した5枚のカードで1枚に俯瞰する構成。全員正解という特殊事情を反映して、サブタイトルには「全員正解の問題」という一言のみを入れ、通常のような単一の正解番号バッジは置かない。

```
Create a Japanese-language infographic, portrait layout, 1080x1920 pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, beige, gray), rounded card sections, consistent with a
modern explainer-graphic aesthetic (icons: an isometric balance scale for
weighing legal requirements, a small car representing a traffic accident,
and an isometric office building representing a company).

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
kanji 謝・属・毀・誉・済・権・賠・償・請・逸・労・限・続, which have
visually similar but structurally different Simplified/Traditional
Chinese counterparts — always draw the standard Japanese (Jōyō) form.

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
Title (large, bold, 2行):
不法行為の損害賠償
誰が請求でき、どう算定するか

Subtitle (smaller, centered, 1行):
令和6年度 第34問　全員正解の問題

（タイトル・サブタイトルのすぐ下にカード群を続ける。導入イラスト・導入文の
ブロックは置かない。）

--- COLUMN A HEADER (pill-shaped badge, color: green) ---
誰が損害を請求できるか

--- COLUMN A, CARD 1 ---
Badge: a filled green circle containing the number 1.
Heading (bold, ONE line, ~20 characters or fewer):
固有の慰謝料請求権は父母配偶者子に限る
Illustration: An isometric balance scale. On one side, three small
figures labeled「父母」「配偶者」「子」stand together with a checkmark.
On the other side, a wider circle labeled「相続人」containing additional
figures labeled「兄弟姉妹」「直系尊属」with a question mark, showing that
the wider circle of heirs is not automatically covered.
Conclusion tag (green banner below the illustration, 5-15 characters):
父母配偶者子に限定

--- COLUMN A, CARD 2 ---
Badge: a filled green circle containing the number 2.
Heading (bold, ONE line, ~20 characters or fewer):
法人の名誉毀損にも無形の損害賠償
Illustration: An isometric office building with a lowered「信用」banner
representing damaged reputation, next to a balance scale holding a coin
stack labeled「財産的損害」on one side and a small cracked shield labeled
「名誉」on the other side, both sides level with a checkmark above.
Conclusion tag (green banner below the illustration, 5-15 characters):
無形の損害も賠償

--- COLUMN A, CARD 3 ---
Badge: a filled green circle containing the number 3.
Heading (bold, ONE line, ~20 characters or fewer):
経済的一体性があれば会社も請求できる
Illustration: An isometric small car involved in a traffic accident with
a figure labeled「代表者」falling, connected by a two-headed arrow labeled
「経済的一体」to an office building labeled「会社」, with a checkmark
between the car scene and the building.
Conclusion tag (green banner below the illustration, 5-15 characters):
会社も賠償請求可

--- COLUMN B HEADER (pill-shaped badge, color: blue) ---
損害をどう算定するか

--- COLUMN B, CARD 4 ---
Badge: a filled blue circle containing the number 4.
Heading (bold, ONE line, ~20 characters or fewer):
逸失利益は一時金でも定期金でも請求できる
Illustration: An isometric balance scale perfectly level, with a single
coin stack labeled「一時金」on one side and a row of smaller repeating
coin stacks labeled「定期金」on the other side, both sides equally
weighted with a checkmark above.
Conclusion tag (blue banner below the illustration, 5-15 characters):
定期金も選べる

--- COLUMN B, CARD 5 ---
Badge: a filled blue circle containing the number 5.
Heading (bold, ONE line, ~20 characters or fewer):
死亡は原則就労可能期間に影響しない
Illustration: An isometric small car involved in a traffic accident,
followed by a horizontal timeline labeled「就労可能期間」that continues
unbroken past a small separate marker labeled「別原因の死亡」, showing the
timeline is not shortened by the later unrelated event.
Conclusion tag (blue banner below the illustration, 5-15 characters):
原則考慮しない

--- FOOTER ---

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional
Chinese, especially 謝・属・毀・誉・済・権・賠・償・請・逸・労・限・続.
If any character renders as a Simplified or Traditional Chinese variant,
redraw that character in the correct Japanese form. Also scan the entire
canvas for any character that is not standard Japanese hiragana,
katakana, or Jōyō kanji — including any Chinese-only character, Korean
Hangul, other non-Japanese script, or stray decorative glyph — and remove
or redraw it so that only standard Japanese text appears anywhere in the
image. Confirm the number of cards equals 5 exactly, with no duplicated
or missing cards, that badge numbers run 1-5 continuously across both
columns without resetting, confirm there is no intro illustration or
paragraph block between the header and the cards, confirm that no card
contains a full sentence of explanatory prose — every card's takeaway
must read as a short heading + a short conclusion tag, at a glance —
confirm that the subtitle names only the year, question number, and the
phrase「全員正解の問題」without stating which single choice is correct,
confirm nothing is rendered below the last card (no summary recap panel,
no trophy or medal icon, no re-listed ○/✕ grid of all 肢, and no
additional text block of any kind — the poster ends immediately after the
last card), and confirm the entire canvas, edge to edge, is filled with a
fully opaque background with no transparency or alpha channel anywhere.
```

---

## インフォグラフィック プロンプト（1〜5 作図ガイド）

問題文を読んだ瞬間に「何を確認し、どの順番で結論にたどり着くか」を、肢ごとに1パネルずつ示す解き方ガイド。肢1・3・5は複数の条件を順に確認する必要があるため分岐構造を明示し、肢2は単純な一段階の確認、肢4は一時金に限定する明文がないことを確認する一段階の分岐として構成する。

```
Create a Japanese-language infographic, portrait layout, 1080x2600 pixels,
clean flat-design isometric illustration style with soft pastel colors
(blue, green, beige, gray), rounded panel sections, consistent with the
same visual language as the whole-problem poster for this article
(不法行為の損害賠償), but built as a set of 5 diagram-drawing panels (a
"how to sketch this fact pattern, in the right order" study reference)
rather than a quick-reference conclusion poster.

DIAGRAM-GUIDE REQUIREMENT (critical): Each panel's purpose is to show the
reader exactly what diagram they should draw on scratch paper while
reading this type of problem, AND the order in which they should check
conditions to get there — isometric figures of 被害者・近親者・代表者・
法人（会社の建物）interacting with a balance scale for weighing legal
requirements and a small car for traffic accidents. Where a 肢 requires
checking multiple conditions in sequence before reaching a conclusion,
draw the panel's diagram as an actual decision flowchart: diamond-shaped
branch nodes with the condition written on them, Yes/No（はい／いいえ）
branch arrows, and a final conclusion node. Where a 肢 is resolved by a
single check, a labeled illustrative diagram is sufficient — do not force
a flowchart. Unlike a glanceable summary poster, each panel MAY include a
short「着眼点」callout box with 1-2 sentences that state the checking ORDER
in words (e.g. "まず〜を確認し、次に〜を確認します"), not just the
conclusion. Do not include case or precedent numbers (article numbers are
fine); keep the callout text as written below verbatim, and keep every
condition each callout describes faithful to the article's own body text
— do not drop or merge a required element.

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
any characters. Pay special attention to the kanji
毀・誉・営・済・権・請・逸・労・限・続・険・拠, which have visually similar
but structurally different Simplified/Traditional Chinese counterparts —
always draw the standard Japanese (Jōyō) form. Within this English prompt
text, use half-width parentheses ( ) consistently — never open a
parenthetical with a full-width （ and close it with a half-width ), or
vice versa.

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
令和6年度 第34問　作図ガイド（全員正解）

（タイトル・サブタイトルのすぐ下にパネル群を続ける。導入イラスト・導入文の
ブロックは置かない。）

--- PANEL 1（肢1） ---
Badge: a filled circle in green containing the number 1.
Heading (bold, ONE line):
父母配偶者子にあたるかを確認する
Diagram: A decision-tree flowchart on an isometric scene of a balance
scale. Start node（ひし形）: 被害者との関係は父母・配偶者・子のいずれかか？
with a はい arrow leading to a conclusion node reading 711条により固有の
慰謝料請求権が認められる, and a いいえ arrow leading to a conclusion node
reading 相続人であることだけでは当然には認められない。
着眼点 callout (1-2 sentences, verbatim, must state the checking order):
まず被害者との関係が父母・配偶者・子のいずれかであるかを確認し、次にそれ
以外の相続人であっても当然にはこの列挙に含まれないことを確認します。
Conclusion tag (a short colored banner/pill, green, 5-15 Japanese
characters):
父母配偶者子に限定

--- PANEL 2（肢2） ---
Badge: a filled circle in green containing the number 2.
Heading (bold, ONE line):
侵害された対象が名誉かを確認する
Diagram: An isometric office building with a lowered「信用」banner, next
to a balance scale holding a coin stack labeled「財産的損害」on one side
and a small cracked shield labeled「名誉」on the other side, both sides
level with a checkmark above indicating both are compensable regardless
of whether the victim is a company.
着眼点 callout (1-2 sentences, verbatim, must state the checking order):
まず侵害された対象が名誉であるかを確認し、次に侵害された主体が法人で
あることは賠償を否定する理由にならないことを確認します。
Conclusion tag (a short colored banner/pill, green, 5-15 Japanese
characters):
無形の損害も賠償

--- PANEL 3（肢3） ---
Badge: a filled circle in green containing the number 3.
Heading (bold, ONE line):
代替性の欠如と経済的一体性を順に確認する
Diagram: A decision-tree flowchart on an isometric scene of a small car
accident with a figure labeled「代表者」falling. Start node（ひし形）:
個人会社の唯一の代表者で機関としての代替性がないか？with a はい arrow
leading to a second diamond node: 会社と代表者が経済的に一体をなす等の
特段の事情があるか？with a はい arrow leading to a conclusion node reading
会社も営業損害の賠償を請求できる, and a いいえ arrow (from either diamond)
leading to a conclusion node reading 会社は直接には請求できない。
着眼点 callout (1-2 sentences, verbatim, must state the checking order):
まず被害者が個人会社の唯一の代表者であり機関としての代替性がないかを
確認し、次に会社と個人が経済的に一体をなす等の特段の事情があるかを確認
します。
Conclusion tag (a short colored banner/pill, green, 5-15 Japanese
characters):
会社も賠償請求可

--- PANEL 4（肢4） ---
Badge: a filled circle in blue containing the number 4.
Heading (bold, ONE line):
一時金に限定する明文があるかを確認する
Diagram: A decision-tree flowchart on an isometric scene of a balance
scale with a single coin stack labeled「一時金」on one side and repeating
smaller coin stacks labeled「定期金」on the other side. Start node
（ひし形）: 支払方法を一時金に限定する明文の規定があるか？with a いいえ
arrow leading to a conclusion node reading 定期金による賠償も求めることが
できる, and a はい arrow leading to a conclusion node reading 一時金に
限られる（この問題では該当しない）。
着眼点 callout (1-2 sentences, verbatim, must state the checking order):
まず損害賠償の支払方法を一時金に限定する明文の規定があるかを確認し、
次に定期金による賠償を求める余地があることを確認します。
Conclusion tag (a short colored banner/pill, blue, 5-15 Japanese
characters):
定期金も選べる

--- PANEL 5（肢5） ---
Badge: a filled circle in blue containing the number 5.
Heading (bold, ONE line):
特段の事情の有無を確認する
Diagram: A decision-tree flowchart on an isometric scene of a small car
accident, followed by a horizontal timeline labeled「就労可能期間」and a
separate marker labeled「別原因の死亡」. Start node（ひし形）: 事故の時点
で、死亡の原因となる具体的事由が存在し近い将来の死亡が客観的に予測され
ていたか？with a はい arrow leading to a conclusion node reading 就労可能
期間の認定に影響する, and a いいえ arrow leading to a conclusion node
reading 原則として就労可能期間の認定に影響しない。
着眼点 callout (1-2 sentences, verbatim, must state the checking order):
まず事故後に別の原因で死亡したという事実自体を確認し、次に事故当時すで
に近い将来の死亡が客観的に予測されていたなどの特段の事情があるかを確認
します。
Conclusion tag (a short colored banner/pill, blue, 5-15 Japanese
characters):
原則考慮しない

--- FOOTER ---
Small footnote text (bottom of panel, small font, verbatim):
民法709条・710条・711条・722条1項（417条及び417条の2の準用）並びに887条
1項・889条1項・890条に基づく整理です。本問は行政書士試験研究センターに
より選択肢1から5のいずれを選んでも正解として採点された問題です。

Final check before rendering: scan every kanji glyph and confirm it is
standard Japanese (Jōyō) form, not Simplified Chinese and not Traditional
Chinese, paying special attention to
毀・誉・営・済・権・請・逸・労・限・続・険・拠. If any character renders as
a Simplified or Traditional Chinese variant, redraw that character in
the correct Japanese form. Also scan the entire canvas for any character
that is not standard Japanese hiragana, katakana, or Jōyō kanji —
including any Chinese-only character, Korean Hangul, other non-Japanese
script, or stray decorative glyph — and remove or redraw it so that only
standard Japanese text appears anywhere in the image. Confirm the panel
count equals 5 exactly, badge numbers run 1-5 continuously, there is no
intro illustration or paragraph block between the header and the panels,
that Panels 1, 3 and 5 (the multi-condition 肢) are each drawn as an
actual flowchart with branch nodes (not a bare illustration with no
visible decision structure) and that both their はい and いいえ branches
lead to explicit conclusion nodes rather than a looping-back arrow, that
each 着眼点 callout states a checking order rather than only a conclusion
and keeps every required element from the source article distinct (no
merged or dropped requirements), confirm the subtitle names only the
year, question number, and「作図ガイド（全員正解）」without stating which
single choice is correct, confirm nothing is rendered below the last
panel's footnote text (no summary recap panel, no trophy or medal icon,
no re-listed ○/✕ grid of all 肢, and no additional text block of any
kind), and confirm the entire canvas, edge to edge, is filled with a
fully opaque background with no transparency or alpha channel anywhere.
```
