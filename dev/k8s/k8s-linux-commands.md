# Jupyter Notebook Linxuコマンド集

## 前提

- [研究室クラスターの使い方](README.md)

## Linxuコマンドの実行方法

- LinuxコマンドはNotebookのコードセル内で、先頭に`!`をつけて、空白文字を置かずに、コマンドを記述することで実行できます
```
!コマンド
```
- :warning: 多くのLinuxコマンドが実行可能ですので、よく理解していないコマンドの実行は避けてください
 

## Pythonパッケージのインストール

- :bulb: JupyterHubから起動したNotebook内では自由にパッケージをインストールして大丈夫です
- `PACKAGE_NAME`: インストールしたいパッケージ名
  
```
import sys
!{sys.executable} -m pip install PACKAGE_NAME
```

## Linux OS情報の表示

- Notebookを起動したLinux OSの情報

```
!cat /etc/os-release
```
```
NAME="Ubuntu"
VERSION="20.04 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
```

## ファイル一覧の表示

- フォルダ名の前に`./`をつけるようにしましょう
- ホームのフルパスは`/home/jovyan`です（固定・全員共通）

```
!ls -l ./shared
```
```
total 4
-rwxrwxrwx 1 1024 users 110 Jan 23  2020 000-DO-NOT-REDISTRIBUTE-再配布厳禁.txt
-rwxrwxrwx 1 1024 users   0 Jul 13 04:34 000-READ-ONLY-AREA-読み込み専用エリア.txt
drwxrwxrwx 1 1024 users  82 Jun 15 08:15 Datasets
```

```
!ls -l /home/jovyan/shared
```
```
total 4
-rwxrwxrwx 1 1024 users 110 Jan 23  2020 000-DO-NOT-REDISTRIBUTE-再配布厳禁.txt
-rwxrwxrwx 1 1024 users   0 Jul 13 04:34 000-READ-ONLY-AREA-読み込み専用エリア.txt
drwxrwxrwx 1 1024 users  82 Jun 15 08:15 Datasets
```