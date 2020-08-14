# 開発スキル

## PCの設定

### 環境：ThinkPad Eシリーズ・Windows 10 Enterprise・US配列

* [PCの初期設定](pc-initial-setup.md)
* [PCの詳細設定](pc-advanced-settings.md)
* [必須アプリのインストール](pc-essential-apps.md)
* [個別アプリのインストール](pc-advanced-apps.md)
* [アプリのアンインストール（削除）](pc-uninstall.md)
* :warning: [PCの初期化](pc-reset.md)
* :warning: [Windows10のインストール](pc-win10.md)

### 環境：ThinkPad Eシリーズ・Ubuntu 18.04 LTS・US配列

* [Windows10用USBインストーラーの作成](pc-win10-installer-on-ubuntu.md)


## 研究室クラスターの使い方

- :bulb: [研究室クラスターについて](k8s/README.md)
- [研究室クラスターのファイルやデータについて](k8s/README-data.md)
- [目的別研究室クラスター使用手順](k8s/README-index.md)

## PythonとJupyter Lab

* [Pythonのインストール](pc-python.md)
* [Jupyter Labの使い方](pc-jupyterlab.md)

## 仮想マシン

:bulb: `Python`（含 `Jupyter Notebook` / `JupyterLab`）, `Ruby`, `R`, `LaTeX`などはWindows版の安定したアプリがありますので、特に支障がない限りそれらを使うことをおすすめします。

### 簡易版

* [Windows Subsystem for Linux 1 (WSL-1)のインストール](pc-wsl-1.md)

### 本格版

* [VirtualBoxとVagrantのインストール](pc-virtualbox-vagrant.md)
* [Ubuntu 18.04 LTSを使った仮想マシンの作成](vm-ubuntu1804.md)
* [CentOS 7を使った仮想マシンの作成](vm-centos7.md)
* [CentOS 7 + Elasticsearch + Kibanaを持つ仮想マシンの作成](vm-centos7-ek.md)
* [仮想マシンにアプリをインストールする方法](vm-install-apps.md)


## チャットボット

[Slack](https://www.slack.com/)を使った簡単なチャットボットの開発。開発言語はPythonを使います。

- [Pythonのインストール](pc-python.md)
- [Slackのインストールと研究室ワークスペースへの参加](pc-slack.md)
- [grokのインストール](pc-ngrok.md)
- [チャットボットの開発](chatbot-slack-1.md)

## ウェブクローラーの取り扱い

ウェブ上のデータを収集するウェブクローラー（ボット）の利用には細心の注意が必要です。

- [ウェブクローラーとユーザエージェント](web-crawler.md)

## ウェブアプリ開発とHerokuへのデプロイ

PythonのFlaskフレームワークを用いたウェブアプリの開発。データベースにはPostgreSQLを使って、最後はHerokuにデプロイします。

- [Gitのインストール](pc-git.md)
- [Pythonのインストール](pc-python.md)
- [PostgreSQLのインストール](pc-postgresql.md)
- [Flaskを使ったウェブアプリ開発](webapp-flask.md)
- [Herokuへのデプロイ](pc-heroku.md)

## Javaアプリ開発環境

GitHubで公開されているJavaアプリのソースコードを入手し、自分でコンパイルする方法。Solrサーチエンジンを例に、使います。

- [Javaと開発ツールのインストール](pc-java.md)
- [GitHubを使った開発1](github-1.md)
- [Solrのコンパイルと実行](solr.md)
