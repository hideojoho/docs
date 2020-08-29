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
$ cp -R ~/shared/Datasets/k8s/projects/eck ~/playground/projects/your-name/my-eck
$ cd ~/playground/projects/your-name/my-eck
$ ls
eck-1.yaml  eck-3.yaml  eck.ipynb
```

- テスト用設定ファイル`eck-1.yaml`
  - Node: 1
  - HDD: 1Gi

```
apiVersion: elasticsearch.k8s.elastic.co/v1
kind: Elasticsearch
metadata:
  name: my-eck
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
$ kubectl apply -f eck-1.yaml
elasticsearch.elasticsearch.k8s.elastic.co/my-eck created
```

- Elasticsearchのステータスが`green`になるまで待つ

```
$ kubectl get elasticsearch
NAME     HEALTH   NODES   VERSION   PHASE   AGE
my-eck   green    1       7.9.0     Ready   97s
```

- Elasticsearchのログインパスワードを入手する

```
$ kubectl get secret my-eck-es-elastic-user -o=jsonpath='{.data.elastic}' | base64 --decode; echo
```

- ノートブック（`eck.ipynb`）を実行する
  - [eck.ipynb](ipynb/eck.ipynb)

## 本番用環境の実行

- テスト用環境でElasticsearchの使い方を学ぶ
- 準備ができたら以下の本番用設定ファイルをノートブックのターミナルから実行する

### 手順

- 既存インスタンスの停止

```
$ kubectl delete -f eck-1.yaml
elasticsearch.elasticsearch.k8s.elastic.co "my-eck" deleted
```

- 停止の確認

```
$ kubectl get elastisearch
error: the server doesn't have a resource type "elastisearch"
```

- 本番用設定ファイル`eck-3.yaml`
  - Node: 3
  - HDD: 100GB max

```
apiVersion: elasticsearch.k8s.elastic.co/v1
kind: Elasticsearch
metadata:
  name: my-eck
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
kubectl apply -f eck-3.yaml
elasticsearch.elasticsearch.k8s.elastic.co/my-eck created
```

- Elasticsearchのステータスが`green`になるまで待つ
  - Node数が`3`になっていることを確認

```
$ kubectl get elasticsearch
NAME     HEALTH   NODES   VERSION   PHASE   AGE
my-eck   green    3       7.9.0     Ready   97s
```

- Elasticsearchのログインパスワードを入手する

```
$ kubectl get secret my-eck-es-elastic-user -o=jsonpath='{.data.elastic}' | base64 --decode; echo
```

- ノートブック（`eck.ipynb`）を実行する
  - [eck.ipynb](ipynb/eck.ipynb)


### 本番用環境の削除

:warning: 索引ファイル等もすべて消えます。必要なデータは事前にバックアップしておきましょう。

```
$ kubectl delete -f eck-3.yaml
```
