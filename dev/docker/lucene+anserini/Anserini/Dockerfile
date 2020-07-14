# ベースイメージ
FROM hideojoho/lucene:8.5.2
# 作業フォルダ
WORKDIR /work
# イメージ情報
LABEL Maintainer="hideo.joho@gmail.com"
LABEL Version="1.0"
LABEL Description="Anserini 0.9.5 with Apache Lucene 8.5.2, Open JDK 11, and Ubuntu 20.04"
# Anserini 0.9.4をインストール
RUN git clone --recurse-submodules https://github.com/castorini/anserini.git
RUN cd anserini && mvn clean package appassembler:assemble
RUN cd /work/anserini/tools/eval && tar xvfz trec_eval.9.0.4.tar.gz && cd trec_eval.9.0.4 && make
RUN cd /work/anserini/tools/eval/ndeval && make
RUN cd /work
