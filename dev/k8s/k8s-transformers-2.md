# 汎用言語表現モデルの再学習

学習済みの汎用言語表現モデルをベースにして、自分のデータを使ってモデルを再学習（微調整・ファインチューニング）する。

:warning: 作成中

## 前提

- [汎用言語表現モデルの利用](k8s-transformers.md)
- Jupyter Notebookイメージ
  - `hideojoho/jupyter-nvidia`

## 手順

### Transformer

以下は全てJupyter Notebook上で実行する

- `transformers`および`datasets`キャッシュ保存先変数の設定（:bulb: 重要）

```
import os
os.environ['TRANSFORMERS_CACHE'] = '/home/jovyan/playground/projects/transformers'
DATASETS_CACHE_DIR = '/home/jovyan/playground/projects/huggingface/datasets'
```

- パッケージのインストール

```
import sys
!{sys.executable} -m pip install ipywidgets torch transformers datasets
```
```
Collecting torch
  Downloading torch-1.6.0-cp38-cp38-manylinux1_x86_64.whl (748.8 MB)
...
Successfully installed click-7.1.2 filelock-3.0.12 future-0.18.2 joblib-0.16.0 numpy-1.19.1 regex-2020.7.14 sacremoses-0.0.43 sentencepiece-0.1.91 tokenizers-0.8.1rc2 torch-1.6.0 transformers-3.1.0 datasets-1.1.2 dill-0.3.2 multiprocess-0.70.10 pandas-1.1.3 pyarrow-1.0.1 pytz-2020.1 xxhash-2.0.0
```

- パッケージのインポート

```
from __future__ import print_function
import ipywidgets as widgets
```

- データセット一覧の読み込み

```
from datasets import list_datasets
datasets_list = list_datasets()
print(', '.join(dataset for dataset in datasets_list))
```
```
aeslc, ag_news, ai2_arc, allocine, anli, arcd, art, billsum, biomrc, blended_skill_talk, blimp, blog_authorship_corpus, bookcorpus, boolq, break_data, c4, cfq, civil_comments, clue, cmrc2018, cnn_dailymail, coarse_discourse, com_qa, common_gen, commonsense_qa, compguesswhat, conll2000, conll2003, coqa, cornell_movie_dialog, cos_e, cosmos_qa, crd3, crime_and_punish, csv, daily_dialog, definite_pronoun_resolution, discofuse, docred, doqa, drop, eli5, emo, emotion, empathetic_dialogues, eraser_multi_rc, esnli, event2Mind, fever, flores, fquad, gap, germeval_14, gigaword, glue, guardian_authorship, hans, hansards, hellaswag, hotpot_qa, hyperpartisan_news_detection, imdb, iwslt2017, jeopardy, json, kilt_tasks, kilt_wikipedia, kor_nli, lc_quad, librispeech_lm, lince, lm1b, math_dataset, math_qa, matinf, mlqa, mlsum, movie_rationales, ms_marco, multi_news, multi_nli, multi_nli_mismatch, mwsc, natural_questions, newsgroup, newsroom, openbookqa, openwebtext, opinosis, pandas, para_crawl, pg19, piaf, polyglot_ner, qa4mre, qa_zre, qangaroo, qanta, qasc, quarel, quartz, quora, quoref, race, reclor, reddit, reddit_tifu, reuters21578, rotten_tomatoes, scan, scicite, scientific_papers, scifact, sciq, scitail, search_qa, sentiment140, snli, social_bias_frames, social_i_qa, sogou_news, squad, squad_es, squad_it, squad_v1_pt, squad_v2, squadshifts, style_change_detection, super_glue, ted_hrlr, ted_multi, text, tiny_shakespeare, trec, trivia_qa, tydiqa, ubuntu_dialogs_corpus, web_of_science, web_questions, wiki40b, wiki_dpr, wiki_qa, wiki_snippets, wiki_split, wikihow, wikipedia, wikisql, wikitext, winogrande, wiqa, wmt14, wmt15, wmt16, wmt17, wmt18, wmt19, wmt_t2t, wnut_17, x_stance, xcopa, xnli, xquad, xsum, xtreme, yelp_polarity
```

- データセットのダウンロード（:bulb: 上で定義した`DATASETS_CACHE_DIR`を使う）

```
dataset = load_dataset('glue', 'mrpc', split='train', cache_dir=DATASETS_CACHE_DIR)
```

- データセットの件数

```
len(dataset)
```
```
3668
```

- データセットの1件目

```
dataset[0]
```
```
{'idx': 0,
 'label': 1,
 'sentence1': 'Amrozi accused his brother , whom he called " the witness " , of deliberately distorting his evidence .',
 'sentence2': 'Referring to him as only " the witness " , Amrozi accused his brother of deliberately distorting his evidence .'}
 ```

- データセットの構成

```
dataset.features
```
```
{'sentence1': Value(dtype='string', id=None),
 'sentence2': Value(dtype='string', id=None),
 'label': ClassLabel(num_classes=2, names=['not_equivalent', 'equivalent'], names_file=None, id=None),
 'idx': Value(dtype='int32', id=None)}
 ```
 
- `equivalent`ラベルのデータ表示
 
 ```
 dataset.filter(lambda example: example['label'] == dataset.features['label'].str2int('equivalent'))[0]
 ```
 ```
 HBox(children=(FloatProgress(value=0.0, max=4.0), HTML(value='')))

{'idx': 0,
 'label': 1,
 'sentence1': 'Amrozi accused his brother , whom he called " the witness " , of deliberately distorting his evidence .',
 'sentence2': 'Referring to him as only " the witness " , Amrozi accused his brother of deliberately distorting his evidence .'}
 ```

 - `not_equivalent`ラベルのデータ表示
 
 ```
 dataset.filter(lambda example: example['label'] == dataset.features['label'].str2int('not_equivalent'))[0]
 ```
 ```
 HBox(children=(FloatProgress(value=0.0, max=4.0), HTML(value='')))

{'idx': 1,
 'label': 0,
 'sentence1': "Yucaipa owned Dominick 's before selling the chain to Safeway in 1998 for $ 2.5 billion .",
 'sentence2': "Yucaipa bought Dominick 's in 1995 for $ 693 million and sold it to Safeway for $ 1.8 billion in 1998 ."}
 ```

- 続く


## URLs

- https://huggingface.co/docs/datasets/quicktour.html

