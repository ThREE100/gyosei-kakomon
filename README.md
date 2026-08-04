# gyosei-kakomon

行政書士試験の過去問演習PWA(個人学習用)。ビルド不要の素のHTML/CSS/JavaScript。

- **公開URL**: https://three100.github.io/gyosei-kakomon/
- **ホスティング**: GitHub Pages(このリポジトリの `main` ブランチを配信)

## 使い方

`index.html` を静的配信するだけで動作する(ビルド工程なし)。ローカル確認は
任意の静的サーバー(例: `npx serve .`)で `index.html` を開く。

## 詳細

構成・データ形式・技術スタックの詳細は [`ARCHITECTURE.md`](./ARCHITECTURE.md) を参照。

## データ

問題データは `data/exam.json`(本試験形式)・`data/oneliner.json`(一問一答)。
再生成用スクリプトは `../scripts/`(このリポジトリの外、プロジェクトルート側)にある。

## 関連

株式会社スリー全体のリポジトリ一覧・全社ルールは [`ThREE100/three-ai-team`](https://github.com/ThREE100/three-ai-team/blob/main/リポジトリ一覧.md) を参照。
