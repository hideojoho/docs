# 汎用言語表現モデルの利用

`BERT`などの汎用言語表現モデルを使って、感情分析、要約、テキスト生成、エンティティ抽出、質問応答などの自然言語処理タスクを行う

- [モデルの再学習](k8s-transformers-2.md)

## 前提

- Jupyter Notebookイメージ
  - モデルの利用：`jupyter/minimal-notebook`

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

### 感情分析

- 感情分析パイプラインの起動

```
classifier = pipeline('sentiment-analysis')
```

- 感情分析の実行

```
classifier('We are very happy to show you the Transformers library.')
```
```
[{'label': 'POSITIVE', 'score': 0.9997795224189758}]
```

### 質問応答

- 質問応答パイプラインの起動

```
qa = pipeline("question-answering")
```

- 文脈情報の定義

```
context = r"""
Extractive Question Answering is the task of extracting an answer from a text given a question. An example of a
question answering dataset is the SQuAD dataset, which is entirely based on that task. If you would like to fine-tune
a model on a SQuAD task, you may leverage the examples/question-answering/run_squad.py script.
"""
```

- 質問応答の実行と回答の表示

```
result = qa(question="What is extractive question answering?", context=context)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")
```
```
Answer: 'the task of extracting an answer from a text given a question.', score: 0.6226, start: 34, end: 96
```

### テキスト生成

- テキスト生成パイプラインの起動

```
text_generator = pipeline("text-generation")
```

- テキスト生成の実行

```
print(text_generator("As far as I am concerned, I will", max_length=50, do_sample=False))
```
```
Setting `pad_token_id` to 50256 (first `eos_token_id`) to generate sequence
[{'generated_text': 'As far as I am concerned, I will be the first to admit that I am not a fan of the idea of a "free market." I think that the idea of a free market is a bit of a stretch. I think that the idea'}]
```

### エンティティ抽出

- エンティティ抽出パイプラインの起動

```
ner = pipeline("ner")
```

- 入力文の作成

```
sequence = "Hugging Face Inc. is a company based in New York City. Its headquarters are in DUMBO, therefore very" "close to the Manhattan Bridge which is visible from the window."
```

- エンティティ抽出の実行と結果表示

```
print(ner(sequence))
```
```
[{'word': 'Hu', 'score': 0.9995632767677307, 'entity': 'I-ORG', 'index': 1}, {'word': '##gging', 'score': 0.9915938973426819, 'entity': 'I-ORG', 'index': 2}, {'word': 'Face', 'score': 0.9982671737670898, 'entity': 'I-ORG', 'index': 3}, {'word': 'Inc', 'score': 0.9994403719902039, 'entity': 'I-ORG', 'index': 4}, {'word': 'New', 'score': 0.9994346499443054, 'entity': 'I-LOC', 'index': 11}, {'word': 'York', 'score': 0.9993270635604858, 'entity': 'I-LOC', 'index': 12}, {'word': 'City', 'score': 0.9993864893913269, 'entity': 'I-LOC', 'index': 13}, {'word': 'D', 'score': 0.9825621843338013, 'entity': 'I-LOC', 'index': 19}, {'word': '##UM', 'score': 0.9369831681251526, 'entity': 'I-LOC', 'index': 20}, {'word': '##BO', 'score': 0.898710310459137, 'entity': 'I-LOC', 'index': 21}, {'word': 'Manhattan', 'score': 0.9758240580558777, 'entity': 'I-LOC', 'index': 29}, {'word': 'Bridge', 'score': 0.9902493953704834, 'entity': 'I-LOC', 'index': 30}]
```

### 要約

- 要約パイプラインの起動

```
summarizer = pipeline("summarization")
```

- 入力文の作成

```
ARTICLE = """ New York (CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, New York.
A year later, she got married again in Westchester County, but to a different man and without divorcing her first husband.
Only 18 days after that marriage, she got hitched yet again. Then, Barrientos declared "I do" five more times, sometimes only within two weeks of each other.
In 2010, she married once more, this time in the Bronx. In an application for a marriage license, she stated it was her "first and only" marriage.
Barrientos, now 39, is facing two criminal counts of "offering a false instrument for filing in the first degree," referring to her false statements on the
2010 marriage license application, according to court documents.
Prosecutors said the marriages were part of an immigration scam.
On Friday, she pleaded not guilty at State Supreme Court in the Bronx, according to her attorney, Christopher Wright, who declined to comment further.
After leaving court, Barrientos was arrested and charged with theft of service and criminal trespass for allegedly sneaking into the New York subway through an emergency exit, said Detective
Annette Markowski, a police spokeswoman. In total, Barrientos has been married 10 times, with nine of her marriages occurring between 1999 and 2002.
All occurred either in Westchester County, Long Island, New Jersey or the Bronx. She is believed to still be married to four men, and at one time, she was married to eight men at once, prosecutors say.
Prosecutors said the immigration scam involved some of her husbands, who filed for permanent residence status shortly after the marriages.
Any divorces happened only after such filings were approved. It was unclear whether any of the men will be prosecuted.
The case was referred to the Bronx District Attorney\'s Office by Immigration and Customs Enforcement and the Department of Homeland Security\'s
Investigation Division. Seven of the men are from so-called "red-flagged" countries, including Egypt, Turkey, Georgia, Pakistan and Mali.
Her eighth husband, Rashid Rajput, was deported in 2006 to his native Pakistan after an investigation by the Joint Terrorism Task Force.
If convicted, Barrientos faces up to four years in prison.  Her next court appearance is scheduled for May 18.
"""
```

- 要約の実行と結果の表示

```
print(summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False))
```
```
[{'summary_text': ' Liana Barrientos, 39, is charged with two counts of "offering a false instrument for filing in the first degree" In total, she has been married 10 times, with nine of her marriages occurring between 1999 and 2002 . At one time, she was married to eight men at once, prosecutors say .'}]
```

## 日本語モデルの利用

- パッケージのインストール

```
import sys
!{sys.executable} -m pip install fugashi ipadic
```

- パッケージのインポート

```
import fugashi
import ipadic
```

### 感情分析

- パッケージのインポート

```
from transformers import AutoTokenizer, AutoModelForSequenceClassification
```

- 日本語モデルのロード

```
tokenizer = AutoTokenizer.from_pretrained("cl-tohoku/bert-base-japanese-whole-word-masking")
model = AutoModelForSequenceClassification.from_pretrained("cl-tohoku/bert-base-japanese-whole-word-masking")
```

- 感情分析パイプラインの起動

```
classifier = pipeline(model=model, tokenizer=tokenizer, task='sentiment-analysis')
```

- 感情分析の実行

```
classifier('トランスフォーマーライブラリを紹介できて、とても幸せです。')
```
```
[{'label': 'LABEL_1', 'score': 0.6203145980834961}]
```

## モデルの再学習

学習済みのモデルをベースに、独自データを使ってモデルを再学習（ファインチューニング）する方法

- [モデルの再学習](k8s-transformers-2.md)

## URLs

- https://huggingface.co/transformers/quicktour.html
- https://huggingface.co/transformers/task_summary.html
- https://github.com/huggingface/transformers/tree/master/notebooks

