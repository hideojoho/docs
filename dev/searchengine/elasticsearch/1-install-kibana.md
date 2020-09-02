# Kibanaのインストールと基本利用

:bulb: Elasticsearch

## 準備

### Javaのインストール

- [Java環境](../../pc-java.md)
- [Elasticsearch](1-install.md)
  
## バイナリのダウンロード

- [Kibanaホームページ](https://www.elastic.co/jp/downloads/kibana)から`WINDOWS`を選択
  - 以下の説明ではバージョン番号を自分がダウンロードしたものに置き換えること
- ダウンロードしたZipファイルを解凍
- 解凍されたフォルダ（例：`kibana-7.9.0-windows-x86_64`）を[第2作業エリア](../../pc-workspace.md)（例 `C:\Home\sNNNNNN`）に移動
- Change the folder name to `kibana-7.9.0`

## 環境変数の設定

- `Ctrl+S`で検索窓を開き、`env`と入力 → 「システム環境変数の編集」を選択
- 「システムプロパティ」ウィンドウが開くので、「詳細設定」タブの一番下にある「環境変数」を選択
- 「ユーザの環境変数」パネルの下から「新規」を選択
- 以下を入力し、OK
  - 変数名：`KIBANA_HOME`
  - 変数値：`C:\Home\sNNNNNNN\kibana-7.9.0`

## Kibanaの起動

- :bulb: Start [Elasticsearch](1-install.md) first
- `Windows PowerShell`を新規起動し、以下のコマンドを実行

```
PS C:\Users\ユーザ名> cd C:\Home\sNNNNNNN\kibana-7.9.0
PS C:\Home\sNNNNNNN\kibana-7.9.0> .\bin\kibana.bat
```

- http://localhost:5601/

## URLs

- https://www.elastic.co/jp/subscriptions
- https://www.elastic.co/guide/en/kibana/current/index.html