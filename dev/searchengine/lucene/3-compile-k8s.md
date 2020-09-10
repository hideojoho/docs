# Luceneソースファイルのコンパイル

研究室クラスターを使ってLuceneのソースコードをコンパイルする手順。

## 前提

- イメージ
  - `hideojoho/jupyter-jdk`
  
## 手順

- 以下の手順はJupyter Labのターミナルで実行します

### tmuxの起動

- コンパイルは時間がかかるので、[tmux](../../k8s/k8s-linux-commands-terminal.md)を使います

```
$ tmux
```

### プロジェクトフォルダの準備

- 以下の手順はtmux内で実行します
- プロジェクトフォルダ：`playground/projects/sNNNNNNN/`

```
$ cd playground/projects/sNNNNNNN
$ mkdir github && cd github
```

### `Lucene/Solr`レポジトリのクローン

```
$ git clone https://github.com/apache/lucene-solr.git
```

### `Lucene`本体のコンパイル

- 10分弱かかります

```
$ cd lucene-solr
$ ./gradlew -p lucene assemble
```

### 文書のコンパイル

- 後で索引付け対象文書として使用します

```
$ ./gradlew -p lucene documentation
```

### `CLASSPATH`の設定

- ビルドされたライブラリ一覧の表示

```
$ find . -name "*-SNAPSHOT.jar" | grep ^\./lucene
./lucene/analysis/common/build/libs/lucene-analyzers-common-9.0.0-SNAPSHOT.jar
./lucene/analysis/icu/build/libs/lucene-analyzers-icu-9.0.0-SNAPSHOT.jar
./lucene/analysis/kuromoji/build/libs/lucene-analyzers-kuromoji-9.0.0-SNAPSHOT.jar
./lucene/analysis/morfologik/build/libs/lucene-analyzers-morfologik-9.0.0-SNAPSHOT.jar
...
```

- `CLASSPATH`の定義
  - `set-classpath.sh`を以下の内容で新規作成
  - `9.0.0`等のバージョン番号は先の一覧に表示されたものに合わせる

```
#!/bin/sh
export CLASSPATH="/home/jovyan/playground/projects/sNNNNNNN/github/lucene-solr/lucene/analysis/common/build/libs/lucene-analyzers-common-9.0.0-SNAPSHOT.jar:/home/jovyan/playground/projects/sNNNNNNN/github/lucene-solr/lucene/core/build/libs/lucene-core-9.0.0-SNAPSHOT.jar:/home/jovyan/playground/projects/sNNNNNNN/github/lucene-solr/lucene/demo/build/libs/lucene-demo-9.0.0-SNAPSHOT.jar:/home/jovyan/playground/projects/sNNNNNNN/github/lucene-solr/lucene/queryparser/build/libs/lucene-queryparser-9.0.0-SNAPSHOT.jar"
```

- `CLASSPATH`の設定と確認

```
$ source set-classpath.sh
$ echo $CLASSPATH
/home/jovyan/playground/projects/sNNNNNNN/github/lucene-solr/lucene/analysis/common/build/libs/lucene-analyzers-common-9.0.0-SNAPSHOT.jar:/home/jovyan/playground/projects/sNNNNNNN/github/lucene-solr/lucene/core/build/libs/lucene-core-9.0.0-SNAPSHOT.jar:/home/jovyan/playground/projects/sNNNNNNN/github/lucene-solr/lucene/demo/build/libs/lucene-demo-9.0.0-SNAPSHOT.jar:/home/jovyan/playground/projects/sNNNNNNN/github/lucene-solr/lucene/queryparser/build/libs/lucene-queryparser-9.0.0-SNAPSHOT.jar
```

## 索引と検索の実行

- テスト

```
$ java org.apache.lucene.demo.IndexFiles
Usage: java org.apache.lucene.demo.IndexFiles [-index INDEX_PATH] [-docs DOCS_PATH] [-update]

This indexes the documents in DOCS_PATH, creating a Lucene indexin INDEX_PATH that can be searched with SearchFiles
```

- ビルドした`Lucene`文書の一部を索引付け

```
$ java org.apache.lucene.demo.IndexFiles -docs lucene/build/documentation/changes
Indexing to directory 'index'...
adding lucene/build/documentation/changes/Changes.html
adding lucene/build/documentation/changes/ChangesFancyStyle.css
adding lucene/build/documentation/changes/ChangesFixedWidthStyle.css
adding lucene/build/documentation/changes/ChangesSimpleStyle.css
837 total milliseconds
```

- 索引ファイルの確認

```
$ ls -l index
total 412
-rw-r--r-- 1 1024 users    415 Sep 10 07:28 _0.cfe
-rw-r--r-- 1 1024 users 406686 Sep 10 07:28 _0.cfs
-rw-r--r-- 1 1024 users    415 Sep 10 07:28 _0.si
-rw-r--r-- 1 1024 users    154 Sep 10 07:28 segments_1
-rw-r--r-- 1 1024 users      0 Sep 10 07:28 write.lock
```

- 検索
  - クエリ：`style`
  
```
$ java org.apache.lucene.demo.SearchFiles
Enter query: 
style
Searching for: style
1 total matching documents
1. lucene/build/documentation/changes/Changes.html
Press (q)uit or enter number to jump to a page.
```

## URLs

- https://lucene.apache.org/core/quickstart.html
- https://lucene.apache.org/core/8_6_1/index.html
