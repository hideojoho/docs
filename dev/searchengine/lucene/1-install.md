# Luceneのインストールと基本利用

## 準備

## Javaのインストール

- [Java環境](../../pc-java.md)
  
### 作業用フォルダの作成

- [第2作業エリア](../../pc-workspace.md)に作業用フォルダ（`Lucene`）を作成
```
PS C:\Users\アカウント名> mkdir C:\Home\sNNNNNNN\Workspace\Lucene
```

## バイナリのダウンロード

- [Luceneホームページ](https://lucene.apache.org/core/downloads.html)から最新版Binary releases（`lucene-8.x.x.zip`）をダウンロード
  - 以下の説明ではバージョン番号を自分がダウンロードしたものに置き換えること
- ダウンロードしたZipファイルを解凍
- 解答されたフォルダ（例、`lucene-8.6.1`）を[第2作業エリア](../../pc-workspace.md)（例 `C:\Home\sNNNNNN`）に移動

## CLASSPATHの設定

- `Ctrl+S`で検索窓を開き、`env`と入力 → 「システム環境変数の編集」を選択
- 「システムプロパティ」ウィンドウが開くので、「詳細設定」タブの一番下にある「環境変数」を選択
- 「ユーザの環境変数」パネルの下から「新規」を選択
- 以下を入力し、OK
  - 変数名：`CLASSPATH`
  - 変数値：`C:\Home\sNNNNNNN\lucene-8.6.1\core\lucene-core-8.6.1.jar;C:\Home\sNNNNNNN\lucene-8.6.1\queryparser\lucene-queryparser-8.6.1.jar;C:\Home\sNNNNNNN\lucene-8.6.1\demo\lucene-demo-8.6.1.jar;C:\Home\sNNNNNNN\lucene-8.6.1\analysis\common\lucene-analyzers-common-8.6.1.jar;%CLASSPATH%`


## 文書の索引付け

- Luceneのマニュアルを索引付けする

```
PS C:\Users\アカウント名> cd C:\Home\sNNNNNNN\Workspace\Lucene
PS C:\Home\sNNNNNNN\Workspace\Lucene> java org.apache.lucene.demo.IndexFiles -docs C:\Home\sNNNNNNN\lucene-8.6.1\docs\changes

Indexing to directory 'index'...
adding C:\Home\sNNNNNNN\lucene-8.6.1\docs\changes\Changes.html
adding C:\Home\sNNNNNNN\lucene-8.6.1\docs\changes\ChangesFancyStyle.css
adding C:\Home\sNNNNNNN\lucene-8.6.1\docs\changes\ChangesFixedWidthStyle.css
adding C:\Home\sNNNNNNN\lucene-8.6.1\docs\changes\ChangesSimpleStyle.css
983 total milliseconds
```

- 確認

```
PS C:\Home\sNNNNNNN\Workspace\Lucene> ls index

  Directory: C:\Home\sNNNNNNN\Workspace\Lucene\index

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---          2020/08/31    19:18            415 _0.cfe
-a---          2020/08/31    19:18         401179 _0.cfs
-a---          2020/08/31    19:18            374 _0.si
-a---          2020/08/31    19:18            154 segments_1
-a---          2020/08/31    19:18              0 write.lock
```

## 文書の検索

- クエリ：`style`
  
```
PS C:\Home\sNNNNNNN\Workspace\Lucene> java org.apache.lucene.demo.SearchFiles

Enter query:
style
Searching for: style
1 total matching documents
1. C:\Home\sNNNNNNN\lucene-8.6.1\docs\changes\Changes.html
Press (q)uit or enter number to jump to a page.
```

## URLs

- https://lucene.apache.org/core/quickstart.html
- https://lucene.apache.org/core/8_6_1/index.html