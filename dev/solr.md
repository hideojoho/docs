# Solrの開発

Solrのソースコードをフォークして、コンパイルする手順。ランク学習機能をONする方法も説明。

## 前提

- [Javaと開発ツールのインストール](pc-java.md)
- [GitHubを使った開発1](github-1.md)

## 所要時間

- 1時間

## フォークとクローン

- [aparch/lucene-solrのレポジトリ](https://github.com/apache/lucene-solr)にいく
- [GitHubを使った開発1](github-1.md)の手順にしたがって、レポジトリをフォークして、手元のPCにクローンする
- `releases/lucene-solr/8.6.0`ブランチを選択

## ソースファイルのコンパイル

以下はクローンしたレポジトリフォルダをVSCodeで開いていることを前提にしています。

- `` Ctrl+Shift+` ``でVSCode内でターミナルを起動
- 以下のコマンドを実行し、ソースコード全体をコンパイル（:information_source: 15分ぐらいかかる）
  - コンパイル中は大量のメッセージが表示されるので、`-p`オプションを追加して、エラーや警告のみを表示するようにしています。
  - より詳細なメッセージを見たい場合は、`-p`オプションなしで実行してみてください
```
PS C:\Home\sNNNNNNN\Workspace\GitHub\lucene-solr> ant compile -p
```
- `BUILD SUCCESS`等のメッセージが表示されたら成功です
- `solr`フォルダに移動し、以下のコマンドを実行することで、`solr`のバイナリファイルを生成（:information_source: 5分ぐらいかかる）
```
PS C:\Home\sNNNNNNN\Workspace\GitHub\lucene-solr> cd solr
PS C:\Home\sNNNNNNN\Workspace\GitHub\lucene-solr\solr> ant server -p
```
- `BUILD SUCCESS`等のメッセージが表示されたら成功です

## `Solr`の実行と停止

- 以下のコマンドを実行し、コンパイルした`solr`を起動
```
PS C:\Home\sNNNNNNN\Workspace\GitHub\lucene-solr\solr> .\bin\solr.cmd start
OpenJDK 64-Bit Server VM warning: JVM cannot use large page memory because it does not have enough privilege to lock pages in memory.Waiting up to 30 to see Solr running on port 8983
Started Solr server on port 8983. Happy searching!
```
- http://localhost:8983/ に移動し、`solr`の起動を確認
- `solr`を停止する場合は、以下のコマンドを実行
```
PS C:\Home\sNNNNNNN\Workspace\GitHub\lucene-solr\solr> .\bin\solr.cmd stop -p 8983
```

## ランク学習機能をONにした`solr`の起動

- ランク学習機能をONにしつつ、`techproducts`というサンプルコーパスを索引付けする
- 詳細：https://lucene.apache.org/solr/guide/8_6/learning-to-rank.html

```
PS C:\Home\sNNNNNNN\Workspace\GitHub\lucene-solr\solr> .\bin\solr.cmd start -e techproducts -Dsolr.ltr.enabled=true
```

- http://localhost:8983/ に移動し、`JVM`の`Args`に`-Dsolr.ltr.enabled=true`が追加されていることを確認

## 機能の変更・追加

- ソースコードをよく読み、理解し、変更を加える
- ソースコードをコンパイルする
- `Solr`を再起動し、変更内容をテストする

## `Solr`の複数インスタンスの起動

`Solr`サーバは、複数のインスタンスを同時起動することができます。各インスタンスには異なるポート番号を指定します。

- デフォルトサーバの起動（ポート番号：`8983`）
```
PS C:\Home\sNNNNNNN\Workspace\GitHub\lucene-solr\solr> .\bin\solr.cmd start
```
- ランク学習用サーバの起動（ポート番号：`8984`）
```
PS C:\Home\sNNNNNNN\Workspace\GitHub\lucene-solr\solr> .\bin\solr.cmd start -e techproducts -Dsolr.ltr.enabled=true -p 8984
```
- サーバの停止
```
PS C:\Home\sNNNNNNN\Workspace\GitHub\lucene-solr\solr> .\bin\solr.cmd stop -p 8983
PS C:\Home\sNNNNNNN\Workspace\GitHub\lucene-solr\solr> .\bin\solr.cmd stop -p 8984
```
