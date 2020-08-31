# Bing Web検索のUIクライアント（チャットボット）

## 準備

### 作業用フォルダの作成

- [第2作業エリア](../../pc-workspace.md)に作業用フォルダ（`BotFrameComposer`）を作成
```
PS C:\Users\アカウント名> mkdir C:\Home\sNNNNNNN\Workspace\BotFrameComposer
```

### Bing Search APIサーバ

- [APIクライアントサーバの構築](1-install.md)
  - http://localhost:5000/
```
{
  "status": "Ready"
}
```

### ソフトウェアのインストール

- 以下のソフトウェアをインストールする
  - .NET Core SDK v3.1.401 https://dotnet.microsoft.com/download
  - Bot Framework Composer v1.0.2 https://github.com/microsoft/BotFramework-Composer/releases/
  - Bot Framework Emulator v4.10.0 https://github.com/Microsoft/BotFramework-Emulator/releases


## チャットボットクライアントの構築

### Bot Framework Composer（BFC）の起動

- 「New」を選択
- `Create from scratch` > `Next`
  - Name: `BingSearchBot-1`
  - Description: `Simple Bing Search Bot`
  - Location: `C:\Home\sNNNNNNN\Workspace\BotFrameComposer`
  - 「OK」を選択

### 挨拶の編集

- 左パネルから`Greeting`を選択
- 中央パネルから`Send a response`を選択
- 右パネルの`Language Generation`を以下の内容に変更（先頭の「-」は必須）

```
- こんにちは。私はBing検索チャットボットです。「SEARCH」と入力して検索を開始してください。
```
- 挨拶の確認
  - BFC画面右上の`Start Bot`を選択
  - セキュリティの警告がでたら、「アクセスを許可する」
  - しばらくすると`Start Bot`のとなりに`Test in Emulator`と表示されるので、選択
  - エミュレータが起動し、挨拶が表示されることを確認

### 検索ダイアログの追加

- 中央パネル上部メニュー > `Add` > `Add new dialog`を選択
  - Name: `getSearch`
  - 「OK」を選択
- 中央パネルに新しく表示された`BeginDialog`の「+」シンボルを選択 > `Send a response`
右パネルの`Language Generation`を以下の内容に変更

```
- それではウェブ検索を始めましょう。
```

### 検索ダイアログへの接続

- 左パネルから`BingSearchBot-1`を選択
- 中央パネル上部メニュー > `Add` > `Add new trigger on BingSearchBot-1`を選択し、以下を入力
  - What is the name of this trigger (RegEx): `search`
  - Please input regex pattern: `search`
  - 「Submit」を選択
- 中央パネルに新しく表示された`Search`の「+」を選択 > `Dialog management` > `Begin a new dialog`
- 右パネルの`Dialog Name`から`getSearch`を選択
- 接続の確認
  - BFC画面右上の`Restart Bot`を選択
  - `Reloading`表示が消えたら、エミュレータに移動し、チャット画面上部の「Restart Conversation - New User ID」を選択
  - 挨拶メッセージが表示されたら、「search」と入力
  - 「それではウェブ検索を始めましょう。」メッセージが表示されることを確認


### クエリの取得

- 左パネルから`getSearch`を選択
- 中央パネル「それではウェブ検索を始めましょう。」の下にある「+」を選択 > `Ask a question` > `Text`を選択
- 右パネルの`Prompt for text`を以下の内容に変更

```
- 検索キーワードを入力してください。
```

- 右パネルのタブを`User Input`に変更し、以下を入力
  - Property:
    - `string`
    - `user.query`
  - Output format: 
    - `expression`
    - `=trim(this.value)`

### 検索結果の取得

- 中央パネルの一番下にある「+」を選択 > `Access external resources` > `Send an HTTP request`を選択
- 右パネルを以下のように変更
  - HTTP method: `GET`
  - Url: `http://localhost:5000/?q=${user.query}`
  - Result property: `dialog.api_response`
- 中央パネルの一番下にある「+」を選択 > `Create a condition` > `Branch: if/else`を選択
- 右パネルの`Condition`に以下の内容を入力

```
dialog.api_response.statusCode == 200
```

- 中央パネルの「True」の下にある「+」を選択 > `Manage properties` > `Set a Property`を選択
- 右パネルを以下のように変更
  - Property: `dialog.search`
  - Value: `=dialog.api_response.content`
- 中央パネルの「Set a Property」の下にある「+」を選択 > `Send a response.`を選択
- 右パネルの`Language Generation`を以下の内容に変更

```
[ThumbnailCard
    title = ${dialog.search.response[0].title}
    subtitle = ${dialog.search.response[0].url}
    text = ${dialog.search.response[0].snippet}
]
```

### エラーの対処

- 中央パネルの「False」の下にある「+」を選択 > `Send a response` を選択
- 右パネルの`Language Generation`を以下の内容に変更

```
- エラー：${dialog.api_response.content.message}
```

- 中央パネルの「False」と「Send a response」の下に「+」を選択 > `Manage properties ` > `Delete a property` を選択
- 右パネルの`Property`に`user.query`を入力

### 検索の確認

- BFC画面右上の`Restart Bot`を選択
- `Reloading`表示が消えたら、エミュレータに移動し、チャット画面上部の「Restart Conversation - New User ID」を選択
- 挨拶メッセージが表示されたら、「search」と入力
- 「それではウェブ検索を始めましょう。」メッセージが表示された後に、「-検索キーワードを入力してください。」と表示されることを確認
- 検索キーワードを入力
- 検索結果の１番目の文書情報がカード形式で表示されることを確認
- 別のキーワードを試すには、「Restart Conversation - New User ID」を選択して、ダイアログをやり直す

## 発展のアイディア

- 検索結果がない場合のエラー対応
- 続けて検索できるようにセッション機能を実装する
- [多機能版APIクライアントサーバ](../../acs-bingsearch-python.md)に切り替えて、チャットの中で検索カテゴリの指定や変更ができるようにする
- チャットボットにパーソナリティを持たせる

## URLs

- https://docs.microsoft.com/en-us/composer/
- https://docs.microsoft.com/en-us/composer/tutorial/tutorial-create-bot