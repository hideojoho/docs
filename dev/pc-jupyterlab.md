# JupyterLabの使い方

## 環境

- Python ver 3.8.3
- JupyterLab ver 2.1.2

## インストール

- [Pythonをインストールする](pc-python.md)
- [JupyterLabをインストールする](pc-python.md)
- [Node.jsをインストールする](https://nodejs.org/ja/)

## 起動

- Windows PowerShellから以下のコマンドを実行
```
C:\Users\アカウント名> py -m jupyter lab
```
- ブラウザが自動的に起動し、Jupyter Labの画面が表示される
  
## 停止

- Jupyter Lab > File > Shut Down

## 拡張機能の追加

- Jupyter Labの左パネルにのパズルピースのようなアイコンを選択
- `Enable`を選択
- 個々の拡張機能の追加方法は以下の「目次機能の追加」を参照

## 目次機能の追加

- 拡張機能パネルに表示される`Discover`パネルから`@jupyterlab/toc`を見つけ、`Install`を選択
- しばらくするとパネル上部に「A bulid is needed ...」メッセージが表示されるので、`Rebulid`を選択
- しばらくすると「Build Complete」ボックスが表示されるので、`Reload`を選択
- 左パネルに目次を表示する拡張機能アイコンが追加されたことを確認
- 他の拡張機能も同様の手順でインストールできる
