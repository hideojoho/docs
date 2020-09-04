# 目的別研究室クラスター利用手順

## 前提

以下の文書をよく読んで理解している。

- [研究室クラスターNotebookの使い方](README-notebook.md)
- [研究室クラスターのファイルやデータについて](README-data.md)

## Pythonパッケージのインストール

- :bulb: JupyterHubから起動したNotebook内では自由にパッケージをインストールして大丈夫です
- `PACKAGE_NAME`: インストールしたいパッケージ名
  
```
import sys
!{sys.executable} -m pip install PACKAGE_NAME
```

## 目的別手順

- [Linuxコマンド集](k8s-linux-commands.md)
- [MySQLデータベースの利用](k8s-mysql.md)
- [Elasticsearchの利用](k8s-elasticsearch.md)
- [Kibanaの利用](k8s-kibana.md)
- [Rayの利用](k8s-ray.md)
