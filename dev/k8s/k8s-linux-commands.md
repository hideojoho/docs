# Jupyter Notebook Linxuコマンド集

## 前提

- [研究室クラスターの使い方](README.md)

## Linxuコマンドの実行方法

- LinuxコマンドはNotebookのコードセル内で、先頭に`!`をつけて、空白文字を置かずに、コマンドを記述することで実行できます
- :warning: 多くのLinuxコマンドが実行可能ですので、よく理解していないコマンドの実行は避けてください
 
## ファイル一覧の表示

```
[ ]: !ls -l ./playground
total 0
-rwxrwxrwx 1 root root   0 Jul 20 03:00 please-make-your-folder-under-projects
drwxrwxrwx 1 root root 102 Aug  7 09:08 projects
```
```
[ ]: !ls -l ./shared
total 4
-rwxrwxrwx 1 1024 users 110 Jan 23  2020 000-DO-NOT-REDISTRIBUTE-再配布厳禁.txt
-rwxrwxrwx 1 1024 users   0 Jul 13 04:34 000-READ-ONLY-AREA-読み込み専用エリア.txt
drwxrwxrwx 1 1024 users  82 Jun 15 08:15 Datasets
```
