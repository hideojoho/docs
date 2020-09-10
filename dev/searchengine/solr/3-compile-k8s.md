# Solrのソースコードのコンパイル

研究室クラスターを使ったSolrのソースコードをコンパイルする方法


## 前提

- [Luceneのソースコードをコンパイルする方法](../lucene/3-compile-k8s.md)

## 手順

- 以下の手順は、Jupyter Labのターミナル内で実行した`tmux`内で実行します


### Solr本体のコンパイル

- 5分間程度かかります

```
$ ./gradlew -p solr assemble
```

### Solrの実行

```
$ cd solr/packaging/build/solr-9.0.0-SNAPSHOT
$ ./bin/solr start
NOTE: Please install lsof as this script needs it to determine if Solr is listening on port 8983.

Started Solr server on port 8983 (pid=1360). Happy searching
```

- 確認

```
$ curl -s "http://localhost:8983/solr/"
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html ng-app="solrAdminApp" ng-csp>
<!--
Licensed to the Apache Software Foundation (ASF) under one or more
...
```

### Solrの停止

```
$ ./bin/solr stop -p 8983
Sending stop command to Solr running on port 8983 ... waiting up to 180 seconds to allow Jetty process 1360 to stop gracefully.
```
