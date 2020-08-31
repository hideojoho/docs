# Elasticsearchの利用

自分専用のElasticsearchインスタンスを作成して、大規模文書の索引付けや検索をする方法

:bulb: 小規模な開発は研究室PCを用いましょう

## 前提

- 指導教員に`kubectl`のコンフィグファイル作成を依頼
  - `sNNNNNNN-k8s-config`
- Jupyter Notebookイメージ
  - `hideojoho/jupyter-kubectl`を選択

## テスト用環境の実行
:bulb: 以下のコマンドをJupyter Notebook内のターミナルから実行する

- `kubectl`の準備（新規ノートブックサーバ起動時に毎回実行）

```
$ mkdir ~/.kube
$ cp ~/shared/Datasets/k8s/certs/sNNNNNNN-k8s-config ~/.kube/config
```

- コンフィグファイルの動作確認
```
$ kubectl get all
No resources found in sNNNNNNN namespace.
```

- プロジェクトフォルダの作成 (e.g., `your-name/my-eck`)（初回のみ実行）
  - `your-name`の例
    - `sNNNNNNN`: 学籍番号
    - `hideojoho`: フルネーム

```
$ cp ~/shared/Datasets/k8s/projects/eck/* ~/playground/projects/your-name/my-eck
$ cd ~/playground/projects/your-name/my-eck
$ ls
es-1.yaml  es-3.yaml  es.ipynb  ingress-kbn.yaml  kbn-1.yaml
```

- テスト用設定ファイル`es-1.yaml`
  - Node: 1
  - HDD: 1Gi

```
apiVersion: elasticsearch.k8s.elastic.co/v1
kind: Elasticsearch
metadata:
  name: my-es
spec:
  version: 7.9.0
  nodeSets:
  - name: default
    count: 1
    config:
      node.master: true
      node.data: true
      node.ingest: true
      node.store.allow_mmap: false
```

- 実行

```
$ kubectl apply -f es-1.yaml
elasticsearch.elasticsearch.k8s.elastic.co/my-es created
```

- Elasticsearchのステータスが`green`になるまで待つ

```
$ kubectl get elasticsearch
NAME     HEALTH   NODES   VERSION   PHASE   AGE
my-es   green    1       7.9.0     Ready   97s
```

- Elasticsearchのログインパスワードを入手する

```
$ kubectl get secret my-es-es-elastic-user -o=jsonpath='{.data.elastic}' | base64 --decode; echo
```

- ノートブック（`es.ipynb`）を実行する
  - [es.ipynb](ipynb/es.ipynb)

## 本番用環境の実行

- テスト用環境でElasticsearchの使い方を学ぶ
- 準備ができたら以下の本番用設定ファイルをノートブックのターミナルから実行する

### 手順

- 既存インスタンスの停止

```
$ kubectl delete -f es-1.yaml
elasticsearch.elasticsearch.k8s.elastic.co "my-es" deleted
```

- 停止の確認

```
$ kubectl get elastisearch
error: the server doesn't have a resource type "elastisearch"
```

- 本番用設定ファイル`es-3.yaml`
  - Node: 3
  - HDD: 100GB max

```
apiVersion: elasticsearch.k8s.elastic.co/v1
kind: Elasticsearch
metadata:
  name: my-es
spec:
  version: 7.9.0
  nodeSets:
  - name: default
    count: 3
    config:
      node.master: true
      node.data: true
      node.ingest: true
      node.store.allow_mmap: false
    volumeClaimTemplates:
    - metadata:
        name: elasticsearch-data
      spec:
        accessModes:
        - ReadWriteOnce
        resources:
          requests:
            storage: 100Gi
        storageClassName: nfs
```

- 実行

```
kubectl apply -f es-3.yaml
elasticsearch.elasticsearch.k8s.elastic.co/my-es created
```

- Elasticsearchのステータスが`green`になるまで待つ
  - Node数が`3`になっていることを確認

```
$ kubectl get elasticsearch
NAME     HEALTH   NODES   VERSION   PHASE   AGE
my-es   green    3       7.9.0     Ready   97s
```

- Elasticsearchのログインパスワードを入手する

```
$ kubectl get secret my-es-es-elastic-user -o=jsonpath='{.data.elastic}' | base64 --decode; echo
```

- ノートブック（`es.ipynb`）を実行する
  - [es.ipynb](ipynb/es.ipynb)


### 本番用環境の削除

:warning: 索引ファイル等もすべて消えます。必要なデータは事前にバックアップしておきましょう。

```
$ kubectl delete -f es-3.yaml
```

## プラグインのインストール

- [日本語アナライザー（kuromoji）](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-kuromoji.html)プラグインの例
- 設定ファイルの変更

```
apiVersion: elasticsearch.k8s.elastic.co/v1
kind: Elasticsearch
metadata:
  name: my-es
spec:
  version: 7.9.0
  nodeSets:
  - name: default
    count: 1
    config:
      node.master: true
      node.data: true
      node.ingest: true
      node.store.allow_mmap: false
    podTemplate:
      spec:
        initContainers:
        - name: install-plugins
          command:
          - sh
          - -c
          - |
            bin/elasticsearch-plugin install analysis-kuromoji
```

- 実行

```
$ kubectl apply -f es-1.yaml
elasticsearch.elasticsearch.k8s.elastic.co/my-es configured
```

- 確認

```
$ kubectl exec -it my-es-es-default-0 -- /usr/share/elasticsearch/bin/elasticsearch-plugin list
analysis-kuromoji
```

## データの可視化と分析

- [Kibanaの利用](k8s-kibana.md)
