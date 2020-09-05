# 汎用言語表現モデルの利用

`BERT`などの汎用言語表現モデルを使って、意見分析、要約、テキスト生成、エンティティ抽出、質問応答などの自然言語処理タスクを行う。

## 前提

- Jupyter Notebookイメージ
  - モデルの利用：`hideojoho/jupyter-minimal`
  - モデルの再学習：`hideojoho/jupyter-nvidia`

## 手順

以下は全てJupyter Notebook上で実行する

- 環境変数の設定

```
import os
os.environ['TRANSFORMERS_CACHE'] = '/home/jovyan/playground/projects/transformers/'
```

- パッケージのインストール

```
import sys
!{sys.executable} -m pip install pytorch transformers
```

- パッケージのインポート

```
from transformers import pipeline
```

- 意見分析

```
classifier = pipeline('sentiment-analysis')
classifier('We are very happy to show you the Transformers library.')
```
```
[{'label': 'POSITIVE', 'score': 0.9997795224189758}]
```
