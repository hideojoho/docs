# Luceneソースファイルのコンパイル

研究室クラスターを使ってLuceneのソースコードをコンパイルする手順。

## 前提

- イメージ
  - `hideojoho/jupyter-jdk`
  
## 手順

- 以下の手順はJupyter Labのターミナルで実行します

### tmuxの起動

- コンパイルは時間がかかるの[tmux](../../k8s/k8s-linux-commands-terminal.md)を使います

```
$ tmux
```

### プロジェクトフォルダに移動

- プロジェクトフォルダ：`playground/projects/sNNNNNNN/`

```
$ cd playground/projects/sNNNNNNN
```

### `Lucene/Solr`レポジトリのクローン

```
$ git clone https://github.com/apache/lucene-solr.git
```

### `Lucene`のコンパイル

- 10分弱かかります

```
$ cd lucene-solr
$ ./gradlew -p lucene assemble
```


## URLs

- https://lucene.apache.org/core/quickstart.html
- https://lucene.apache.org/core/8_6_1/index.html
