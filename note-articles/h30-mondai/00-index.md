# 平成30年度 出題リスト（構成固め用ロードマップ）

全60問中、著作権の都合で**問題1・7・58〜60は公式PDFに問題文が掲載されていない**（正解番号は1＝①、7＝②、58＝①、59＝②、60＝②）。

さらに、**問56（個人情報保護法）は公式正解表で「正答なし」**とされている（PDF本文は掲載されているが、単一の正解を前提とした通常の解説記事が成立しないため、著作権による非掲載とは別の理由でロードマップから除外する）。

以上、**除外6問（問1・7・56・58〜60）**を除く、実際に記事化できる**54問**の一覧が以下。

**データソース**：`data/exam.json`には平成30年度（H30）が収録されていない（収録はR2〜R7のみ）。令和元年度と同様、
著者がアップロードした公式PDF（`h30_mondai.pdf`）本文と、著者が会話に直接貼り付けた公式正解表（択一式60問の正解＋
記述式3問の正解例）を直接照合する。将来`data/exam.json`にH30が追加された場合は、機械的な突合を行うことが望ましい。

**法改正に関する注意**：平成30年度の問題は当時の法令を前提とするが、`note-articles/laws/`のデータは現行法（令和8年時点）である。
民法（平成29年改正・令和元年〜令和4年施行分）・会社法・行政不服審査法・個人情報保護法などは、出題時と現行で条文が
異なる場合がある。公式正解番号は出題時の法令に基づくため、各記事の「確認事項」メモで出題時と現行の差異を明記する。

形式の記号は令和元年度の`00-index.md`と同じ（A＝ア〜オの組合せ／A（変則）＝空欄語句の組合せ／B＝1〜5の単純5択／
多肢選択式／記述式）。

## 内訳

出題形式別：A 18問／B 28問／A（変則） 2問／多肢選択式 3問／記述式 3問

科目別：基礎法学 1問／憲法 5問／行政法 22問／民法 11問／商法 1問／会社法 4問／一般知識等 10問

## 問題一覧

| 問 | 科目 | 形式 | 出題テーマ（記事タイトル用の仮見出し） | 記事ファイル（予定） |
|---|---|---|---|---|
| 2 | 基礎法学 | A | 「法」に関する用語（実定法・実質法・基本法・社会法・準拠法）の正誤の組合せ | [q02-hou-yougo.md](./q02-hou-yougo.md) |
| 3 | 憲法 | B | 百里基地訴訟（最三小判平元.6.20）の一節の空欄補充：憲法98条1項「国務に関するその他の行為」と私法上の行為 | [q03-hyakuri-kichi.md](./q03-hyakuri-kichi.md) |
| 4 | 憲法 | B | 学問の自由（大学の自治・ポポロ事件・旭川学テ）に関する妥当でない記述 | [q04-gakumon-jiyuu.md](./q04-gakumon-jiyuu.md) |
| 5 | 憲法 | B | 生存権（朝日訴訟・堀木訴訟・プログラム規定）に関する判例に照らし妥当な記述 | [q05-seizonken.md](./q05-seizonken.md) |
| 6 | 憲法 | B | 選挙公約（インターネット投票・棄権罰則・参議院の性格）と選挙の諸原則：抵触が問題となり得ない原則 | [q06-senkyo-gensoku.md](./q06-senkyo-gensoku.md) |
| 8 | 行政法 | A | 行政代執行法（費用徴収・戒告・通知・代執行手続）に関する正しい記述の組合せ | [q08-gyousei-daishikkou.md](./q08-gyousei-daishikkou.md) |
| 9 | 行政法 | B | 行政上の法律関係（公営住宅・食品衛生法上の許可・租税滞納処分・建築基準法と民法）に関する判例 | [q09-gyousei-houritsu-kankei.md](./q09-gyousei-houritsu-kankei.md) |
| 10 | 行政法 | B | 行政処分の無効と取消し（無効確認・審査請求・職権取消し・国家賠償）に関する正しい記述 | [q10-shobun-muko-torikeshi.md](./q10-shobun-muko-torikeshi.md) |
| 11 | 行政法 | B | 行政手続法：申請に対する処分と不利益処分の比較（基準・理由提示・標準処理期間・公聴会） | [q11-shinsei-futori-hikaku.md](./q11-shinsei-futori-hikaku.md) |
| 12 | 行政法 | B | 法令違反の是正を求める行政指導（行政手続法）：誤っている記述 | [q12-gyousei-shidou.md](./q12-gyousei-shidou.md) |
| 13 | 行政法 | B | 意見公募手続（命令等・処分基準・行政指導指針）に関する正しい記述 | [q13-iken-koubo.md](./q13-iken-koubo.md) |
| 14 | 行政法 | B | 行政不服審査法：不作為についての審査請求に関する妥当な記述 | [q14-fusakui-shinsaseikyuu.md](./q14-fusakui-shinsaseikyuu.md) |
| 15 | 行政法 | A | 行政不服審査法：審査請求（代理人・標準審理期間・口頭意見陳述・承継・参加人）の正しい記述の組合せ | [q15-shinsaseikyuu.md](./q15-shinsaseikyuu.md) |
| 16 | 行政法 | A（変則） | 行政不服審査法の条文（18条1項・26条・45条1項・59条1項）の空欄補充の組合せ | [q16-gyofuku-jobun-kuuran.md](./q16-gyofuku-jobun-kuuran.md) |
| 17 | 行政法 | B | 許認可等の申請に対する処分の取消判決の効力（第三者効・拘束力）：誤っている記述 | [q17-torikeshi-hanketsu-kouryoku.md](./q17-torikeshi-hanketsu-kouryoku.md) |
| 18 | 行政法 | B | 民衆訴訟と機関訴訟（行政事件訴訟法）に関する法令・判例に照らし妥当な記述 | [q18-minshuu-kikan-soshou.md](./q18-minshuu-kikan-soshou.md) |
| 19 | 行政法 | A（変則） | 差止訴訟（行訴法37条の4）に関する最一小判平28.12.8（厚木基地）の空欄A〜Dの組合せ | [q19-sashitome-soshou.md](./q19-sashitome-soshou.md) |
| 20 | 行政法 | A | 国家賠償法1条（建築確認・パトカー追跡・水俣病認定遅延・更正・学校事故）に関する判例の妥当な組合せ | [q20-kokubaihou-1jou.md](./q20-kokubaihou-1jou.md) |
| 21 | 行政法 | B | 道路用地の収用に係る損失補償に関する正しい記述 | [q21-sonshitsu-hoshou.md](./q21-sonshitsu-hoshou.md) |
| 22 | 行政法 | B | 地方自治法：特別区に関する妥当な記述 | [q22-tokubetsuku.md](./q22-tokubetsuku.md) |
| 23 | 行政法 | A | 地方公共団体の条例と規則（罰則・再議・公の施設・選挙参与）に関する正しい記述の組合せ | [q23-jourei-kisoku.md](./q23-jourei-kisoku.md) |
| 24 | 行政法 | B | 地方自治法：都道府県の事務（自治事務・法定受託事務・監査請求）に関する正しい記述 | [q24-todoufuken-jimu.md](./q24-todoufuken-jimu.md) |
| 25 | 行政法 | B | 道路等についての最高裁判決（騒音・時効取得・一括指定・放置車両・安全認定）に関する正しい記述 | [q25-douro-saikou.md](./q25-douro-saikou.md) |
| 26 | 行政法 | B | 市立保育所廃止条例をめぐる訴訟・直接請求（処分性・住民訴訟・第三者効）に関する妥当な記述 | [q26-hoikusho-haishi-jourei.md](./q26-hoikusho-haishi-jourei.md) |
| 27 | 民法 | B | 公序良俗および強行法規違反に関する妥当でない記述 | [q27-kouryouzokuzoku.md](./q27-kouryouzokuzoku.md) |
| 28 | 民法 | A | 契約の附款（条件・期限・出世払い・条件成就の妨害）に関する妥当な組合せ | [q28-fukan-jouken.md](./q28-fukan-jouken.md) |
| 29 | 民法 | A | 他人物売買・無権代理と相続・共有・仮登記・建物収去土地明渡し（甲土地の売買）に関する妥当な組合せ | [q29-kou-tochi-baibai.md](./q29-kou-tochi-baibai.md) |
| 30 | 民法 | B | 抵当権の効力（従物・借地権・物上代位・利息）に関する妥当な記述 | [q30-teitouken-kouryoku.md](./q30-teitouken-kouryoku.md) |
| 31 | 民法 | B | 弁済（充当・代物弁済・提供・供託）に関する妥当でない記述 | [q31-bensai.md](./q31-bensai.md) |
| 32 | 民法 | A | 使用貸借と賃貸借に共通する事項に関する組合せ | [q32-shiyou-chinshaku.md](./q32-shiyou-chinshaku.md) |
| 33 | 民法 | B | 使用者責任と共同不法行為者間の求償に関する妥当な記述 | [q33-shiyousha-kyoudou-fuhoukoui.md](./q33-shiyousha-kyoudou-fuhoukoui.md) |
| 34 | 民法 | A | 離婚（財産分与・面接交渉・親権者・離婚訴訟・有責配偶者）に関する妥当な組合せ | [q34-rikon.md](./q34-rikon.md) |
| 35 | 民法 | B | 後見（未成年後見・成年後見・後見監督人）に関する妥当な記述 | [q35-koken.md](./q35-koken.md) |
| 36 | 商法 | A | 商人・商行為（代理権・報酬・連帯債務・保証・寄託）に関する誤っている組合せ | [q36-shounin-shoukoui.md](./q36-shounin-shoukoui.md) |
| 37 | 会社法 | A | 株式会社の設立における発起人等の責任に関する誤っている組合せ | [q37-hokkinin-sekinin.md](./q37-hokkinin-sekinin.md) |
| 38 | 会社法 | B | 譲渡制限株式に関する誤っている記述 | [q38-joutoseigen-kabushiki.md](./q38-joutoseigen-kabushiki.md) |
| 39 | 会社法 | B | 社外取締役に関する誤っている記述 | [q39-shagai-torishimariyaku.md](./q39-shagai-torishimariyaku.md) |
| 40 | 会社法 | B | 剰余金の配当に関する正しい記述 | [q40-jouyokin-haitou.md](./q40-jouyokin-haitou.md) |
| 41 | 憲法 | 多肢選択式 | 公務員の政治的自由（国家公務員法102条・最二小判平24.12.7）の空欄補充 | [q41-tashi-kokkakoumuin-seijiteki-koui.md](./q41-tashi-kokkakoumuin-seijiteki-koui.md) |
| 42 | 行政法 | 多肢選択式 | 行政事件訴訟法10条：取消しの理由の制限（自己の法律上の利益・原処分主義）の空欄補充 | [q42-tashi-torikeshi-riyuu-seigen.md](./q42-tashi-torikeshi-riyuu-seigen.md) |
| 43 | 行政法 | 多肢選択式 | 地方公共団体の施策変更と信頼保護（最三小判昭56.1.27）の空欄補充 | [q43-tashi-shisaku-henkou-shinrai.md](./q43-tashi-shisaku-henkou-shinrai.md) |
| 44 | 行政法 | 記述式 | 農地転用許可の申請書不受理：被告と訴訟類型（不作為の違法確認・義務付け訴訟） | [q44-kijutsu-nouchi-tenyou.md](./q44-kijutsu-nouchi-tenyou.md) |
| 45 | 民法 | 記述式 | 成年被後見人との売買契約の追認催告（本件契約を追認するか否かの確答） | [q45-kijutsu-saikoku.md](./q45-kijutsu-saikoku.md) |
| 46 | 民法 | 記述式 | 書面によらない贈与の撤回（民法550条） | [q46-kijutsu-zouyo-tekkai.md](./q46-kijutsu-zouyo-tekkai.md) |
| 47 | 一般知識等 | A | 外国人技能実習制度（2017年11月〜）に関する妥当でない組合せ | [q47-gaikokujin-ginou-jisshuu.md](./q47-gaikokujin-ginou-jisshuu.md) |
| 48 | 一般知識等 | A | 専門資格に関する事務をつかさどる省庁に関する妥当でない組合せ | [q48-senmon-shikaku-shochou.md](./q48-senmon-shikaku-shochou.md) |
| 49 | 一般知識等 | B | 戦後日本の消費生活協同組合に関する妥当な記述 | [q49-seikyou.md](./q49-seikyou.md) |
| 50 | 一般知識等 | B | 近年の日本の貿易および対外直接投資に関する妥当な記述 | [q50-boueki-chokusetsu-toushi.md](./q50-boueki-chokusetsu-toushi.md) |
| 51 | 一般知識等 | B | 墓地・火葬・死体の取扱い（墓地、埋葬等に関する法律）に関する妥当な記述 | [q51-bochi-maisou.md](./q51-bochi-maisou.md) |
| 52 | 一般知識等 | A | 地方自治体の住民等（住民税・住民基本台帳・住所地特例・住所）に関する妥当な組合せ | [q52-juumin.md](./q52-juumin.md) |
| 53 | 一般知識等 | A | 風適法による許可・届出の対象になっていない営業形態の組合せ | [q53-fuutekihou.md](./q53-fuutekihou.md) |
| 54 | 一般知識等 | A | 防犯カメラ（設置規制・個人情報・条例・ガイドライン）に関する妥当でない組合せ | [q54-bouhan-camera.md](./q54-bouhan-camera.md) |
| 55 | 一般知識等 | A | 欧州データ保護規則（GDPR）に関する妥当な組合せ | [q55-gdpr.md](./q55-gdpr.md) |
| 57 | 一般知識等 | A | 個人情報保護法2条2項の「個人識別符号」に関する妥当な組合せ | [q57-kojin-shikibetsu-fugou.md](./q57-kojin-shikibetsu-fugou.md) |
