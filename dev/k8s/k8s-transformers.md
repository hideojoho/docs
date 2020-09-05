# 汎用言語表現モデルの利用

`BERT`などの汎用言語表現モデルを使って、意見分析、要約、テキスト生成、エンティティ抽出、質問応答などの自然言語処理タスクを行う。

## 前提

- Jupyter Notebookイメージ
  - モデルの利用：`jupyter/minimal-notebook`
  - モデルの再学習：`hideojoho/jupyter-nvidia`

## 手順

### 拡張機能を有効にする

:bulb: 以下はノートブックを開く前に行う。開いている場合は、一度シャットダウンしておく。

- Jupyter Labの左端パネルの一番下のパズルアイコンを選択
- `Enable`を選択
- `Discover`リストから`@jupyter-widgets/jupyterlab-manager`の「Install」を選択
- 左パネルの上部に表示される「Rebuild」を選択し、ビルドが終わるまで待つ
- `Build Complete`の表示がでたら、`Reload`を選択
- 新規ノートブックを開く

### Transformer

以下は全てJupyter Notebook上で実行する

- 環境変数の設定

```
import os
os.environ['TRANSFORMERS_CACHE'] = '/home/jovyan/playground/projects/transformers/'
```

- パッケージのインストール

```
import sys
!{sys.executable} -m pip install torch transformers
```
```
Collecting torch
  Downloading torch-1.6.0-cp38-cp38-manylinux1_x86_64.whl (748.8 MB)
...
Successfully installed click-7.1.2 filelock-3.0.12 future-0.18.2 joblib-0.16.0 numpy-1.19.1 regex-2020.7.14 sacremoses-0.0.43 sentencepiece-0.1.91 tokenizers-0.8.1rc2 torch-1.6.0 transformers-3.1.0
```

- パッケージのインポート

```
from transformers import pipeline
```

- 意見分析パイプラインの起動

```
classifier = pipeline('sentiment-analysis')
```

- 意見分析の実行

```
classifier('We are very happy to show you the Transformers library.')
```
```
[{'label': 'POSITIVE', 'score': 0.9997795224189758}]
```

## URLs

- https://huggingface.co/transformers/quicktour.html
