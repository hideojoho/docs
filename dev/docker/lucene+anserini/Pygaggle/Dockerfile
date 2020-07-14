FROM hideojoho/pyserini:0.9.4
# 作業フォルダ
WORKDIR /work
# イメージ情報
LABEL Maintainer="hideo.joho@gmail.com"
LABEL Version="1.0"
LABEL Description="Pygaggle 0.0.1 with Pyserini 0.9.0, Anserini 0.9.5, Apache Lucene 8.5.2, Open JDK 11, and Ubuntu 20.04"
# Pygaggleをインストール
RUN pip3 install scipy==1.4.1 tensorflow==2.2.0 coloredlogs dataclasses numpy==1.18.2 pydantic==1.5 scikit-learn spacy==2.2.4 tensorboard tokenizers==0.5.2 tqdm==4.45.0 torch torchvision transformers==2.7.0 pygaggle==0.0.1 pyserini==0.9.0
