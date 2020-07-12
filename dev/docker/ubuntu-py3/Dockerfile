# ベースイメージ
FROM ubuntu:20.04
# イメージ情報
LABEL Maintainer="YOUR_EMAIL"
LABEL Version="1.0"
LABEL Description="This a sample Dockerfile to learn how to make a Docker image."
# パッケージの更新
RUN apt update && apt -y upgrade
# 開発系パッケージの一括インストール（任意）
RUN apt install -y build-essential
# Pythonとpipのインストール
RUN apt install -y python3 python3-pip
# 不要パッケージとキャッシュの削除
RUN apt autoremove -y && apt clean
