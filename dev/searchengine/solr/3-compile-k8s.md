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

### ランク学習機能の有効化


```
$ ./bin/solr start -e techproducts "-Dsolr.ltr.enabled=true"
Creating Solr home directory /home/jovyan/playground/projects/hideojoho/github/lucene-solr/solr/packaging/build/solr-9.0.0-SNAPSHOT/example/techproducts/solr

Starting up Solr on port 8983 using command:
"bin/solr" start -p 8983 -s "example/techproducts/solr" -Dsolr.ltr.enabled=true

NOTE: Please install lsof as this script needs it to determine if Solr is listening on port 8983.

Started Solr server on port 8983 (pid=404). Happy searching!


Created new core 'techproducts'
Indexing tech product example docs from /home/jovyan/playground/projects/hideojoho/github/lucene-solr/solr/packaging/build/solr-9.0.0-SNAPSHOT/example/exampledocs
SimplePostTool version 5.0.0
Posting files to [base] url http://localhost:8983/solr/techproducts/update using content-type application/xml...
POSTing file gb18030-example.xml to [base]
POSTing file hd.xml to [base]
POSTing file ipod_other.xml to [base]
POSTing file ipod_video.xml to [base]
POSTing file manufacturers.xml to [base]
POSTing file mem.xml to [base]
POSTing file money.xml to [base]
POSTing file monitor.xml to [base]
POSTing file monitor2.xml to [base]
POSTing file mp500.xml to [base]
POSTing file sd500.xml to [base]
POSTing file solr.xml to [base]
POSTing file utf8-example.xml to [base]
POSTing file vidcard.xml to [base]
14 files indexed.
COMMITting Solr index changes to http://localhost:8983/solr/techproducts/update...
Time spent: 0:00:01.003

Solr techproducts example launched successfully. Direct your Web browser to http://localhost:8983/solr to visit the Solr Admin UI
```

- 確認

```
$ curl -s "http://localhost:8983/solr/techproducts/admin/ping"
{
  "responseHeader":{
    "zkConnected":null,
    "status":0,
    "QTime":13,
    "params":{
      "q":"{!lucene}*:*",
      "distrib":"false",
      "df":"text",
      "preferLocalShards":"false",
      "rows":"10",
      "echoParams":"all",
      "rid":"localhost-1"}},
  "status":"OK"}
```
