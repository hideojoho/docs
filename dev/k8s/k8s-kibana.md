# Kibanaの利用

自分専用のKibanaインスタンスを作成して、データの可視化や分析をする方法

:bulb: 小規模な開発は研究室PCを用いましょう

## 前提

- [Elasticsearchの利用](k8s-elasticsearch.md)

## インスタンスのデプロイ

- 設定ファイル`kbn-1.yaml`の編集
  - `<your-app-path>`を`sNNNNNNN-kbn`等に変更する
  - `sNNNNNNN`は学籍番号

```
apiVersion: kibana.k8s.elastic.co/v1
kind: Kibana
metadata:
  name: my-kbn
  namespace: hideo
spec:
  version: 7.9.0
  count: 1
  elasticsearchRef:
    name: my-es
  http:
    tls:
      selfSignedCertificate:
        disabled: true
  podTemplate:
    spec:
      containers:
      - name: kibana
        env:
        - name: SERVER_BASEPATH
          value: "<your-app-path>" # Change to "/sNNNNNNN-kbn"
```

- 実行

```
$ kubectl apply -f kbn-1.yaml
kibana.kibana.k8s.elastic.co/my-kbn created
```

- Kibanaのステータスが`green`になるまで待つ

```
$ kubectl get kibana
NAME     HEALTH   NODES   VERSION   AGE
my-kbn   green    1       7.9.0     106m
```

## インスタンスの公開

- 設定ファイル`ingress-kbn.yaml`を編集
  - `<your-app-path>`を`kbn-1.yaml`と同じパスに変更する

```
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: my-kbn
  labels:
    run: my-kbn
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /$1
spec:
  rules:
  - host: isr.slis.tsukuba.ac.jp
    http:
      paths:
      - path: /<your-app-path>/(.*)$  # Change it to /sNNNNNNN-kbn/(.*)$
        backend:
          serviceName: my-kbn-kb-http
          servicePort: 5601
```

- 実行

```
$ kubectl apply -f ingress-kbn.yaml 
ingress.extensions/my-kbn created
```

## Kibanaへのアクセス

- https://isr.slis.tsukuba.ac.jp/sNNNNNNN-kbn/
  - `sNNNNNNN-kbn`：自分で設定したパス
  - ユーザ名：`elastic`
  - パスワード：以下の手順で入手

```
$ kubectl get secret my-es-es-elastic-user -o=jsonpath='{.data.elastic}' | base64 --decode; echo
```

