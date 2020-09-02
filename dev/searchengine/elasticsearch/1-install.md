# Elasticsearchのインストールと基本利用


## 準備

### Javaのインストール

- [Java環境](../../pc-java.md)
  
## バイナリのダウンロード

- [Elasticsearchホームページ](https://www.elastic.co/jp/downloads/elasticsearch)から`WINDOWS`を選択
  - 以下の説明ではバージョン番号を自分がダウンロードしたものに置き換えること
- ダウンロードしたZipファイルを解凍
- 解凍されたフォルダ（例：`elasticsearch-7.9.0`）を[第2作業エリア](../../pc-workspace.md)（例 `C:\Home\sNNNNNN`）に移動

## 環境変数の設定

- `Ctrl+S`で検索窓を開き、`env`と入力 → 「システム環境変数の編集」を選択
- 「システムプロパティ」ウィンドウが開くので、「詳細設定」タブの一番下にある「環境変数」を選択
- 「ユーザの環境変数」パネルの下から「新規」を選択
- 以下を入力し、OK
  - 変数名：`ES_HOME`
  - 変数値：`C:\Home\sNNNNNNN\elasticsearch-7.9.0`

## Elasticsearchの起動

- `Windows PowerShell`を新規起動し、以下のコマンドを実行

```
PS C:\Users\ユーザ名> cd C:\Home\sNNNNNNN\elasticsearch-7.9.0
PS C:\Home\sNNNNNNN\elasticsearch-7.9.0> .\bin\elasticsearch.bat

[2020-09-02T12:18:11,194][INFO ][o.e.n.Node               ] [DESKTOP-8NHHU5A] version[7.9.0], pid[21044], build[default/zip/a479a2a7fce0389512d6a9361301708b92dff667/2020-08-11T21:36:48.204330Z], OS[Windows 10/10.0/amd64], JVM[Oracle Corporation/Java HotSpot(TM) 64-Bit Server VM/14.0.2/14.0.2+12-46]
...
[2020-09-02T12:18:40,260][INFO ][o.e.l.LicenseService     ] [DESKTOP-8NHHU5A] license [4920fdf5-977e-416b-80a7-87fb8f83d610] mode [basic] - valid
[2020-09-02T12:18:40,262][INFO ][o.e.x.s.s.SecurityStatusChangeListener] [DESKTOP-8NHHU5A] Active license is now [BASIC]; Security is disabled
```

- http://localhost:9200/

```
{
  "name" : "DESKTOP-8NHHU5A",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "zc02j8hARNaiFo8a_lVH7g",
  "version" : {
    "number" : "7.9.0",
    "build_flavor" : "default",
    "build_type" : "zip",
    "build_hash" : "a479a2a7fce0389512d6a9361301708b92dff667",
    "build_date" : "2020-08-11T21:36:48.204330Z",
    "build_snapshot" : false,
    "lucene_version" : "8.6.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

- http://localhost:9200/_cluster/health?pretty

```
{
  "cluster_name" : "elasticsearch",
  "status" : "green",
  "timed_out" : false,
  "number_of_nodes" : 1,
  "number_of_data_nodes" : 1,
  "active_primary_shards" : 0,
  "active_shards" : 0,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 0,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 100.0
}
```

## Stop Elasticsearch

- `Ctrl+C`

```
...
[2020-09-02T12:19:49,624][INFO ][o.e.x.m.p.NativeController] [DESKTOP-8NHHU5A] Native controller process has stopped - no new native processes can be started
[2020-09-02T12:19:49,628][INFO ][o.e.n.Node               ] [DESKTOP-8NHHU5A] stopping ...
[2020-09-02T12:19:49,643][INFO ][o.e.x.w.WatcherService   ] [DESKTOP-8NHHU5A] stopping watch service, reason [shutdown initiated]
[2020-09-02T12:19:49,645][INFO ][o.e.x.w.WatcherLifeCycleService] [DESKTOP-8NHHU5A] watcher has stopped and shutdown
[2020-09-02T12:19:50,041][INFO ][o.e.n.Node               ] [DESKTOP-8NHHU5A] stopped
[2020-09-02T12:19:50,041][INFO ][o.e.n.Node               ] [DESKTOP-8NHHU5A] closing ...
[2020-09-02T12:19:50,053][INFO ][o.e.n.Node               ] [DESKTOP-8NHHU5A] closed
バッチ ジョブを終了しますか (Y/N)? y
```

## Connect from Kibana

- [Kibana](1-install-kibana.md)

## URLs

- https://www.elastic.co/jp/subscriptions
- https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html