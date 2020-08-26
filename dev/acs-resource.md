#  Azureリソースの取得

:bulb: `Freeインスタンス`は一定期間無料ですが、クレジットカードは必要です

## Bing Searchの例

- [Azureポータル](https://portal.azure.com/#home)に移動
- 「リソースの作成」を選択
- 検索窓で`Bing Search`と入力し、結果から「Bing Search」を選択
- 「作成」を選択し、次の画面で以下を入力
  - 名前：`YourName-BingSearch`（例：`Joho-BingSearch`）
  - サブスクリプション：`Azure サブスクリプション１`
  - 価格レベル：`Free F1`
  - リソースグループ
    - 初めての場合
      - 新規作成：`YourName` + `Year` + `Month`（例：`Joho202008`）
    - 作成済みの場合
      - 自分のグループ名を選択（例：`Joho202008`）
  - リソースグループの場所：`(US) 米国西部2`
  - [x] 以下の通知を読み、理解しました。
- 「作成」
- 「デプロイが完了しました」になったら完了


## Free F1 インスタンス

- :warning: [API利用制限](https://azure.microsoft.com/ja-jp/pricing/details/cognitive-services/search-api/)を確認しておくこと。
- Freeインスタンスの上限（あるいは使用期限）に達したら指導教員に相談しましょう。

## リソースの追加取得

別サービスのリソースを追加取得する場合、リソース名は別のものにしますが、リソースグループは既存のものを選択しましょう。