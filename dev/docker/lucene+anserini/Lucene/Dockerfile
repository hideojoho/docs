# ベースイメージ
FROM ubuntu:20.04
# 作業フォルダ
WORKDIR /work
# 何も聞くな
ENV DEBIAN_FRONTEND=noninteractive
# イメージ情報
LABEL Maintainer="hideo.joho@gmail.com"
LABEL Version="1.0"
LABEL Description="Apache Lucene 8.5.2 with Open JDK 11 on Ubuntu 20.04"
# パッケージの更新
RUN apt update && apt -y upgrade
# 開発系パッケージのインストール
RUN apt install -y build-essential curl git
# Open JDK 11とmvnのインストール
RUN apt install -y default-jdk maven
# 不要パッケージとキャッシュの削除
RUN apt autoremove -y && apt clean
# Lucene 8.5.2 をインストール
RUN curl -O "https://ftp.tsukuba.wide.ad.jp/software/apache/lucene/java/8.5.2/lucene-8.5.2.tgz"
RUN tar xvfz lucene-8.5.2.tgz
ENV LUCENE_HOME /work/lucene-8.5.2
ENV CLASSPATH $CLASSPATH:$LUCENE_HOME/core/lucene-core-8.5.2.jar
ENV CLASSPATH $CLASSPATH:$LUCENE_HOME/queryparser/lucene-queryparser-8.5.2.jar
ENV CLASSPATH $CLASSPATH:$LUCENE_HOME/analysis/common/lucene-analyzers-common-8.5.2.jar
ENV CLASSPATH $CLASSPATH:$LUCENE_HOME/demo/lucene-demo-8.5.2.jar
# Set locale
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
