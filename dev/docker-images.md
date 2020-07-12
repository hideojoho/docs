# Dockerイメージの作成

研究室クラスターで再利用可能なDockerイメージを作成し、Docker Hubに登録する方法

## 所要時間

- 1-2時間

## 前提

- WSL2
- Docker for Windows

## 手順

- Dockerfileの作成
- ベースイメージの選定

### Dockerfileの作成

- `C:\Users\アカウント名\Local\Docker`に`MyImage`というフォルダを新規作成
  - これ以降、ファイルは全て`MyImage`に保存する
- `MyImage`にファイル`Dockerfile`を新規作成

### ベースイメージの選定

- 個々のDockerイメージは小さなLinuxバーチャルマシンなので、ベースとなるLinuxシステムを選定する
- 選定するベースシステム（Linuxディストリビューション）によって、Pythonなどのパッケージをインストールするコマンドが異なる
- 以下は[Docker公式の代表的なベースイメージ](https://hub.docker.com/search?q=&type=image&image_filter=official&category=os)からの抜粋

|ベースシステム|特徴|インストールコマンド|Tag（サイズ）|
|:--|:--|:--|:--|
|[alpine](https://hub.docker.com/_/alpine)|小型ベースイメージ|`apk`|[latest (linux/amd64)](https://hub.docker.com/_/alpine?tab=tags&name=latest) (2.66MB)|
|[amazonlinux](https://hub.docker.com/_/amazonlinux)|AWSのECで使用されているOS|[latest (linux/amd64)](https://hub.docker.com/_/amazonlinux?tab=tags&page=1&name=latest) (54.83MB)|
|[ubuntu](https://hub.docker.com/_/ubuntu)|Debianベースの代表的OS|`apt`|[20.04 (linux/amd64)](https://hub.docker.com/_/ubuntu?tab=tags&name=20.04) (27.27MB)|
|[centos](https://hub.docker.com/_/centos)|RedHatベースの代表的OS|`yum`|[latest (linux/amd64)](https://hub.docker.com/_/centos?tab=tags&page=1&name=centos8) (71.4MB)|

## URLs

- http://docs.docker.jp/engine/userguide/dockerimages.html
