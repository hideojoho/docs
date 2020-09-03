# Ray

:bulb: [Ray](https://docs.ray.io/en/latest/index.html)は深層学習プロセスをKubernetesクラスター上で分散処理するミドルウェアです。

## 前提

- 指導教員に`kubectl`のコンフィグファイル作成を依頼
  - `sNNNNNNN-k8s-config`
- Jupyter Notebookイメージ
  - `hideojoho/jupyter-kubectl`を選択
  
## `kubectl`の準備（新規ノートブックサーバ起動時に毎回実行）

以下の処理は、Jupyter Lab上のターミナルから実行

```
$ mkdir ~/.kube
$ cp ~/shared/Datasets/k8s/certs/sNNNNNNN-k8s-config ~/.kube/config
```

- コンフィグファイルの動作確認
```
$ kubectl get all
No resources found in sNNNNNNN namespace.
```

## 作業用フォルダの作成

```
$ mkdir playground/projects/sNNNNNNN/my-ray
```

- ノートブックの作成
  - 左パネルで`playground/projects/sNNNNNNN/my-ray`に移動した後、ノートブックを新規作成


## Ray設定ファイル

以下の処理は、Jupyter Lab上の`playground/projects/sNNNNNNN/my-ray`フォルダに新規作成したノートブックで実行する

- `ray-cluster.yaml`の入手

```
!wget https://raw.githubusercontent.com/ray-project/ray/master/doc/kubernetes/ray-cluster.yaml
```
```
--2020-09-03 13:53:38--  https://raw.githubusercontent.com/ray-project/ray/master/doc/kubernetes/ray-cluster.yaml
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.228.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|151.101.228.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 4612 (4.5K) [text/plain]
Saving to: ‘ray-cluster.yaml’

ray-cluster.yaml  100%[===================>]   4.50K  --.-KB/s    in 0s      

2020-09-03 13:53:39 (39.0 MB/s) - ‘ray-cluster.yaml’ saved [4612/4612]
```

- `ray-cluster.yaml`の編集
  - 左パネルからダウンロードした`ray-cluster.yaml`を選択
  - `namespace: ray` → `namespace: sNNNNNNN` に変更（複数個所あります）

## Rayクラスターのデプロイ

- デプロイ

```
!kubectl apply -f ray-cluster.yaml
```
```
service/ray-head created
deployment.apps/ray-head created
deployment.apps/ray-worker created
```

- 確認
  - `ray-head-xxxxxxx`を後で使う

```
!kubectl get pods
```
```
NAME                          READY   STATUS    RESTARTS   AGE
ray-head-576698bcf-mzm5b      1/1     Running   0          11m
ray-worker-6df9f4bdfd-2n7ch   1/1     Running   1          11m
ray-worker-6df9f4bdfd-htg8b   1/1     Running   1          11m
ray-worker-6df9f4bdfd-xx9rm   1/1     Running   1          11m
```

## Pythonプログラムの準備と実行

- `example.py`の入手

```
!wget https://raw.githubusercontent.com/ray-project/ray/master/doc/kubernetes/example.py
```
```
--2020-09-03 13:54:18--  https://raw.githubusercontent.com/ray-project/ray/master/doc/kubernetes/example.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.228.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|151.101.228.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1498 (1.5K) [text/plain]
Saving to: ‘example.py’

example.py        100%[===================>]   1.46K  --.-KB/s    in 0s      

2020-09-03 13:54:18 (16.9 MB/s) - ‘example.py’ saved [1498/1498]
```

- `example.py`のコピー

```
!kubectl cp example.py ray-head-576698bcf-mzm5b:/example.py
```

- `example.py`の実行

```
!kubectl exec ray-head-576698bcf-mzm5b -- python example.py
```
```
WARNING: Logging before InitGoogleLogging() is written to STDERR
I0903 06:23:59.983279   140   140 global_state_accessor.cc:25] Redis server address = 10.233.59.119:6379, is test flag = 0
I0903 06:23:59.984807   140   140 redis_client.cc:146] RedisClient connected.
I0903 06:23:59.993295   140   140 redis_gcs_client.cc:84] RedisGcsClient Connected.
I0903 06:23:59.994874   140   140 service_based_gcs_client.cc:195] Reconnected to GCS server: 10.233.111.47:36385
I0903 06:23:59.995381   140   140 service_based_accessor.cc:92] Reestablishing subscription for job info.
I0903 06:23:59.995404   140   140 service_based_accessor.cc:422] Reestablishing subscription for actor info.
I0903 06:23:59.995415   140   140 service_based_accessor.cc:808] Reestablishing subscription for node info.
I0903 06:23:59.995434   140   140 service_based_accessor.cc:1084] Reestablishing subscription for task info.
I0903 06:23:59.995443   140   140 service_based_accessor.cc:1259] Reestablishing subscription for object locations.
I0903 06:23:59.995451   140   140 service_based_accessor.cc:1370] Reestablishing subscription for worker failures.
I0903 06:23:59.995469   140   140 service_based_gcs_client.cc:86] ServiceBasedGcsClient Connected.
Iteration 0
Counter({('ray-worker-6df9f4bdfd-htg8b', 'ray-head-576698bcf-mzm5b'): 19, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-htg8b'): 18, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-2n7ch'): 16, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-xx9rm'): 15, ('ray-head-576698bcf-mzm5b', 'ray-head-576698bcf-mzm5b'): 7, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-xx9rm'): 6, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-head-576698bcf-mzm5b'): 4, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-2n7ch'): 4, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-head-576698bcf-mzm5b'): 4, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-htg8b'): 3, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-htg8b'): 1, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-htg8b'): 1, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-2n7ch'): 1, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-2n7ch'): 1})
Iteration 1
Counter({('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-htg8b'): 14, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-2n7ch'): 11, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-xx9rm'): 10, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-2n7ch'): 8, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-xx9rm'): 8, ('ray-worker-6df9f4bdfd-htg8b', 'ray-head-576698bcf-mzm5b'): 8, ('ray-head-576698bcf-mzm5b', 'ray-head-576698bcf-mzm5b'): 7, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-head-576698bcf-mzm5b'): 6, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-htg8b'): 5, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-xx9rm'): 5, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-2n7ch'): 5, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-htg8b'): 5, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-head-576698bcf-mzm5b'): 4, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-xx9rm'): 2, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-2n7ch'): 1, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-htg8b'): 1})
Iteration 2
Counter({('ray-worker-6df9f4bdfd-2n7ch', 'ray-head-576698bcf-mzm5b'): 13, ('ray-head-576698bcf-mzm5b', 'ray-head-576698bcf-mzm5b'): 12, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-htg8b'): 11, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-2n7ch'): 10, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-htg8b'): 9, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-xx9rm'): 9, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-2n7ch'): 8, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-xx9rm'): 8, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-xx9rm'): 6, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-htg8b'): 3, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-2n7ch'): 3, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-head-576698bcf-mzm5b'): 3, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-2n7ch'): 2, ('ray-worker-6df9f4bdfd-htg8b', 'ray-head-576698bcf-mzm5b'): 2, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-xx9rm'): 1})
Iteration 3
Counter({('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-htg8b'): 14, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-xx9rm'): 13, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-2n7ch'): 13, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-head-576698bcf-mzm5b'): 12, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-2n7ch'): 8, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-head-576698bcf-mzm5b'): 7, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-xx9rm'): 6, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-2n7ch'): 5, ('ray-head-576698bcf-mzm5b', 'ray-head-576698bcf-mzm5b'): 4, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-xx9rm'): 4, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-2n7ch'): 3, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-xx9rm'): 3, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-htg8b'): 2, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-htg8b'): 2, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-htg8b'): 2, ('ray-worker-6df9f4bdfd-htg8b', 'ray-head-576698bcf-mzm5b'): 2})
Iteration 4
Counter({('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-htg8b'): 15, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-2n7ch'): 13, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-xx9rm'): 11, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-head-576698bcf-mzm5b'): 10, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-xx9rm'): 9, ('ray-head-576698bcf-mzm5b', 'ray-head-576698bcf-mzm5b'): 8, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-head-576698bcf-mzm5b'): 6, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-2n7ch'): 5, ('ray-worker-6df9f4bdfd-htg8b', 'ray-head-576698bcf-mzm5b'): 5, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-xx9rm'): 5, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-xx9rm'): 4, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-htg8b'): 3, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-2n7ch'): 2, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-htg8b'): 2, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-2n7ch'): 1, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-htg8b'): 1})
Iteration 5
Counter({('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-2n7ch'): 13, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-htg8b'): 11, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-head-576698bcf-mzm5b'): 10, ('ray-worker-6df9f4bdfd-htg8b', 'ray-head-576698bcf-mzm5b'): 8, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-xx9rm'): 7, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-2n7ch'): 7, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-xx9rm'): 7, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-htg8b'): 6, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-2n7ch'): 6, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-xx9rm'): 6, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-htg8b'): 6, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-xx9rm'): 4, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-2n7ch'): 3, ('ray-head-576698bcf-mzm5b', 'ray-head-576698bcf-mzm5b'): 3, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-head-576698bcf-mzm5b'): 2, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-htg8b'): 1})
Iteration 6
Counter({('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-2n7ch'): 18, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-htg8b'): 13, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-xx9rm'): 12, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-head-576698bcf-mzm5b'): 10, ('ray-worker-6df9f4bdfd-htg8b', 'ray-head-576698bcf-mzm5b'): 9, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-htg8b'): 7, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-xx9rm'): 7, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-xx9rm'): 5, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-2n7ch'): 4, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-2n7ch'): 3, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-htg8b'): 3, ('ray-head-576698bcf-mzm5b', 'ray-head-576698bcf-mzm5b'): 3, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-htg8b'): 3, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-head-576698bcf-mzm5b'): 2, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-2n7ch'): 1})
Iteration 7
Counter({('ray-worker-6df9f4bdfd-htg8b', 'ray-head-576698bcf-mzm5b'): 17, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-xx9rm'): 16, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-htg8b'): 10, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-2n7ch'): 10, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-2n7ch'): 8, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-2n7ch'): 7, ('ray-head-576698bcf-mzm5b', 'ray-head-576698bcf-mzm5b'): 6, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-htg8b'): 5, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-xx9rm'): 5, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-htg8b'): 5, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-xx9rm'): 5, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-htg8b'): 4, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-xx9rm'): 1, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-head-576698bcf-mzm5b'): 1})
Iteration 8
Counter({('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-2n7ch'): 17, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-htg8b'): 10, ('ray-worker-6df9f4bdfd-htg8b', 'ray-head-576698bcf-mzm5b'): 10, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-xx9rm'): 9, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-htg8b'): 8, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-2n7ch'): 5, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-htg8b'): 5, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-head-576698bcf-mzm5b'): 5, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-head-576698bcf-mzm5b'): 5, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-2n7ch'): 5, ('ray-head-576698bcf-mzm5b', 'ray-head-576698bcf-mzm5b'): 5, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-xx9rm'): 5, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-htg8b'): 4, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-xx9rm'): 3, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-xx9rm'): 2, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-2n7ch'): 2})
Iteration 9
Counter({('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-htg8b'): 14, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-2n7ch'): 13, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-head-576698bcf-mzm5b'): 10, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-xx9rm'): 7, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-xx9rm'): 7, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-htg8b'): 7, ('ray-head-576698bcf-mzm5b', 'ray-head-576698bcf-mzm5b'): 6, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-xx9rm'): 6, ('ray-worker-6df9f4bdfd-htg8b', 'ray-worker-6df9f4bdfd-2n7ch'): 6, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-2n7ch'): 6, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-2n7ch'): 5, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-head-576698bcf-mzm5b'): 4, ('ray-worker-6df9f4bdfd-htg8b', 'ray-head-576698bcf-mzm5b'): 4, ('ray-head-576698bcf-mzm5b', 'ray-worker-6df9f4bdfd-xx9rm'): 3, ('ray-worker-6df9f4bdfd-2n7ch', 'ray-worker-6df9f4bdfd-htg8b'): 1, ('ray-worker-6df9f4bdfd-xx9rm', 'ray-worker-6df9f4bdfd-htg8b'): 1})
Success!
```

## Rayクラスターの削除

```
!kubectl delete -f ray-cluster.yaml
```
```
service "ray-head" deleted
deployment.apps "ray-head" deleted
deployment.apps "ray-worker" deleted
```

## URLs

- https://docs.ray.io/en/latest/cluster/kubernetes.html
- https://github.com/ray-project/ray/tree/master/doc/kubernetes
