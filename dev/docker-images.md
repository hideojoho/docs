# Dockerイメージの作成

再利用可能なDockerイメージを作成し、Docker Hubに登録する方法

## 所要時間

- 1-2時間

## 前提

- WSL2
- Docker for Windows
- VSCode + Remote WSLプラグイン
- Docker Hubアカウント（個人のDockerイメージを公開する場合のみ）

## 手順

- 作業フォルダとVSCodeの準備
- ベースイメージの選定

### 作業フォルダの作成

- `C:\Users\アカウント名\Local\Docker`に`MyImage`というフォルダを新規作成
  - これ以降、ファイルは全て`MyImage`に保存する
  
### VSCodeの準備

- `MyImage`フォルダをVSCodeで開く
- `Ctrl+Shift+P` → `wsl`と入力し、`Remote-WSL: Reopen Folder in Windows`を選択
  - `Select dstro`: `Ubuntu 20-04`を選択
  - ウインドウがリロードされて、左パネルのフォルダ名に`MYIMAGE [WSL:UBUNTU-20.04]`と表示されることを確認
- ``Ctrl+Shift+` ``でVSCodeのターミナルを開き、Windowsの`PowerShell`ではなく、WSLのShellが起動していることを確認

```
$ uname -a
Linux DESKTOP-34R6FTL 4.19.104-microsoft-standard #1 SMP Wed Feb 19 06:37:35 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```

### ベースイメージの選定

- 個々のDockerイメージは小さなLinuxバーチャルマシン（もしくはそのプロセス）なので、ベースとなるLinuxシステムを選定する
- 選定するベースシステム（Linuxディストリビューション）によって、Pythonなどのパッケージをインストールするコマンドが異なる
- 以下は[Docker公式の代表的なベースイメージ](https://hub.docker.com/search?q=&type=image&image_filter=official&category=os)からの抜粋

|ベースシステム|特徴|インストールコマンド|Tag（サイズ）|
|:--|:--|:--|:--|
|[alpine](https://hub.docker.com/_/alpine)|小型ベースイメージ|`apk`|[latest (linux/amd64)](https://hub.docker.com/_/alpine?tab=tags&name=latest) (2.66MB)|
|[amazonlinux](https://hub.docker.com/_/amazonlinux)|AWSのEC2で使用されているOS|`yum`|[latest (linux/amd64)](https://hub.docker.com/_/amazonlinux?tab=tags&page=1&name=latest) (54.83MB)|
|[ubuntu](https://hub.docker.com/_/ubuntu)|Debianベースの代表的OS|`apt`|[20.04 (linux/amd64)](https://hub.docker.com/_/ubuntu?tab=tags&name=20.04) (27.27MB)|
|[centos](https://hub.docker.com/_/centos)|RedHatベースの代表的OS|`yum`|[latest (linux/amd64)](https://hub.docker.com/_/centos?tab=tags&page=1&name=centos8) (71.4MB)|

### サンプルDockerイメージ構成

- 今回の以下の構成のDockerイメージを作成します。
  - ベースOS: [Ubuntu 20.04](https://hub.docker.com/_/ubuntu?tab=tags&name=20.04)
  - Python
- `MyImage`にファイル`Dockerfile`を新規作成

```
# ベースイメージ
FROM ubuntu:20.04
# イメージ作成者情報
MAINTAINER Your Name <yourname@example.com>
# パッケージの更新
RUN apt update && apt -y upgrade
# 開発系パッケージの一括インストール（任意）
RUN apt install -y build-essential
# Pythonとpipのインストール
RUN apt install -y python3 python3-pip
# 不要パッケージとキャッシュの削除
RUN apt autoremove -y && apt clean
```

### Dockerイメージの構築

- VSCodeのターミナル（WSL）で以下のコマンドを実行
  - `myimage`: ユーザ名（任意、Docker Hub個人アカウント名、あるいは`joholab`）
  - `ubuntu_py3`: イメージ名
  - `20200712`: イメージのバージョンタグ（今回は日付を使用）
  - `.`: `Dockerfile`の場所

```
$ docker build -t myimage/ubuntu-py3:20200712 .
...
...
Successfully built 60f1a341a261
Successfully tagged myimage/ubuntu-py3:20200712
```

### 作成されたDockerイメージの確認

```
$ docker images
REPOSITORY                   TAG                 IMAGE ID            CREATED             SIZE
myimage/ubuntu-py3           20200712            60f1a341a261        33 seconds ago      391MB
```

### Dockerイメージの削除（ホストPC）

```
$ docker rmi [IMAGE ID]
```

### DockerイメージのDocker Hubへの送信

- 個人的なDockerイメージをDocker Hubに公開する場合は、Docker Hubアカウントを作成します
- Dockerイメージ構築コマンドで、ユーザ名の部分で、アカウント名を指定する

```
$ docker push ユーザ名/イメージ名
```

### 研究室用Dockerイメージを作成する際の注意点

- ユーザ名：`joholab`
- イメージ名：他のイメージと競合しないように、指導教員に相談してください
- Docker Hubへの送信：指導教員に相談してください

## URLs

- http://docs.docker.jp/engine/userguide/dockerimages.html
