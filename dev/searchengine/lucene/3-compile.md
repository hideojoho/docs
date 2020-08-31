# Luceneソースファイルのコンパイル

Luceneのソースコードをフォークして、コンパイルする手順。

## 前提

- [Javaと開発ツールのインストール](../../pc-java.md)
- [GitHubを使った開発1](../../github-1.md)


## フォークとクローン

- [aparch/lucene-solrのレポジトリ](https://github.com/apache/lucene-solr)にいく
- [GitHubを使った開発1](../.../github-1.md)の手順にしたがって、レポジトリをフォークして、手元のPCにクローンする

## ソースファイルのコンパイル

以下はクローンしたレポジトリフォルダをVSCodeで開いていることを前提にしています。

- `releases/lucene-solr/8.6.0`ブランチを選択
- `` Ctrl+Shift+` ``でVSCode内でターミナルを起動
- 以下のコマンドを実行し、`lucene-core`ソースコードをコンパイル（:information_source: 15分ぐらいかかる）
  - コンパイル中は大量のメッセージが表示されるので、`-q`オプションを追加して、エラーや警告のみを表示するようにしています。
  - より詳細なメッセージを見たい場合は、`-q`オプションなしで実行してみてください
```
PS C:\Home\sNNNNNNN\Workspace\GitHub\lucene-solr> ant compile-core -q
```
- `BUILD SUCCESS`等のメッセージが表示されたら成功です

## コンパイルしたLuceneの利用

- [Luceneのインストールと基本利用](1-install.md)の手順の内、環境変数`CLASSPATH`の設定を変更する
- 以下は、`8.6.0`のブランチをコンパイルした例

  - `C:\Home\sNNNNNNN\Workspace\GitHub\lucene-solr\lucene\build\core\lucene-core-8.6.0-SNAPSHOT.jar`
  - `C:\Home\sNNNNNNN\Workspace\GitHub\lucene-solr\lucene\build\queryparser\lucene-queryparser-8.6.0-SNAPSHOT.jar`
  - `C:\Home\sNNNNNNN\Workspace\GitHub\lucene-solr\lucene\build\demo\lucene-demo-8.6.0-SNAPSHOT.jar`
  - `C:\Home\sNNNNNNN\Workspace\GitHub\lucene-solr\lucene\build\analysis\common\lucene-analyzers-common-8.6.0-SNAPSHOT.jar`