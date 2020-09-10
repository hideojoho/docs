# Solrのソースコードのコンパイル

研究室クラスターを使ったSolrのソースコードをコンパイルする方法


## 前提

- [Luceneのソースコードをコンパイルする方法](../lucene/3-compile-k8s.md)

## 手順

- 以下の手順は、Jupyter Labのターミナル内で実行した`tmux`内で実行します


### Solrのコンパイル

- 5分間程度かかります

```
$ ./gradlew -p solr assemble
```
