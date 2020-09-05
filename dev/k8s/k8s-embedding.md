# 分散表現の取得

ある語の分散表現の値を取得する方法。学習済みのモデルを用いる。

:bulb: 取得できる語彙やベクトルの形状は学習済みモデルに依存します。

## 前提

- Jupyter Notebookイメージ
  - `hideojoho/jupyter-minimal`を選択

## 手順

以下は全てJupyter Notebook上で実行する

- `gensim`パッケージのインストール

```
import sys
!{sys.executable} -m pip install gensim
```
```
Collecting gensim
  Downloading gensim-3.8.3-cp38-cp38-manylinux1_x86_64.whl (24.2 MB)
     |████████████████████████████████| 24.2 MB 8.4 MB/s eta 0:00:01    |█████████▍                      | 7.1 MB 8.4 MB/s eta 0:00:03
...
Installing collected packages: boto, docutils, jmespath, botocore, s3transfer, boto3, smart-open, numpy, scipy, gensim
Successfully installed boto-2.49.0 boto3-1.14.56 botocore-1.17.56 docutils-0.15.2 gensim-3.8.3 jmespath-0.10.0 numpy-1.19.1 s3transfer-0.3.3 scipy-1.5.2 smart-open-2.1.1
```

- `gensim`パッケージのインポート

```
import gensim
```

- 学習済みモデル一覧

```
!find shared/Datasets/embedding/ | grep bin
```
```
shared/Datasets/embedding/ja/tohoku/entity_vector/entity_vector.model.bin
```

- モデルの選択と読み込み
  - 少し時間がかかります

```
model_path = "~/shared/Datasets/embedding/ja/tohoku/entity_vector/entity_vector.model.bin"
model = gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=True)
```

- 分散表現の獲得
  
```
model["東京"]
```
```
array([-4.9377084e-01, -1.0795103e+00, -1.7043670e+00, -2.8346848e-01,
...
        1.5249516e-01, -4.6106954e+00,  6.3850349e-01,  4.3945411e-01],
      dtype=float32)
```

- 概念演算
  - 「日本」（という国）から「東京」（という首都）を引いて、「ロンドン」（という首都）を足すと？

```
model.most_similar(positive=['日本', 'ロンドン'], negative=['東京'])
```
```
[('イギリス', 0.7616775035858154),
 ('[イギリス]', 0.7135626077651978),
 ('英国', 0.7128424048423767),
 ('アメリカ', 0.7063097953796387),
 ('アメリカ合衆国', 0.6884847283363342),
 ('ヨーロッパ', 0.6529363989830017),
 ('フランス', 0.6480700969696045),
 ('[英国]', 0.644333004951477),
 ('[アメリカ]', 0.6354398131370544),
 ('[アメリカ合衆国]', 0.6236234307289124)]
 ```
