# 汎用言語表現モデルの再学習

学習済みの汎用言語表現モデルをベースにして、自分のデータを使ってモデルを再学習（微調整・ファインチューニング）する。

## 前提

- [汎用言語表現モデルの利用](k8s-transformers.md)
- Jupyter Notebookイメージ
  - `hideojoho/jupyter-nvidia`

## 手順

### Transformer

以下は全てJupyter Notebook上で実行する

- 環境変数の設定（:bulb: 重要）

```
import os
os.environ['TRANSFORMERS_CACHE'] = '/home/jovyan/playground/projects/transformers/'
```

- パッケージのインストール

```
import sys
!{sys.executable} -m pip install ipywidgets torch transformers
```
```
Collecting torch
  Downloading torch-1.6.0-cp38-cp38-manylinux1_x86_64.whl (748.8 MB)
...
Successfully installed click-7.1.2 filelock-3.0.12 future-0.18.2 joblib-0.16.0 numpy-1.19.1 regex-2020.7.14 sacremoses-0.0.43 sentencepiece-0.1.91 tokenizers-0.8.1rc2 torch-1.6.0 transformers-3.1.0
```

- パッケージのインポート

```
from __future__ import print_function
import ipywidgets as widgets
from transformers import pipeline
```


## URLs

- https://huggingface.co/transformers/training.html

