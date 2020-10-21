# Python

:bulb: 2020年5月現在では、[Anaconda](pc-anacoda.md)よりも、本ページで説明している実行環境を推奨します。

## 所要時間

- 30分

## インストール

- [Python Releases for Windows](https://www.python.org/downloads/windows/)にいく
- `Download Windows x86-64 executable installer`を選択しインストーラーをダウンロード → 起動
- インストーラーの初期画面で以下にチェックを入れる
  - [x] Install launcher for all users (recommended)
  - [x] Add Python 3.x to PATH
- `Customize installation`を選択 → `Next`
- `Advanced Options`の`Customize install location`の`C:\Users\ユーザ名\AppData\Local\Programs\Python\Python38`を`C:\Home\sNNNNNN\Python\Python38`に変更 → `Install`
- `Setup was successful`が表示されたら、`Close`
- `Windows PowerShell`を起動し、以下のコマンドを実行
```
PS C:\Users\アカウント名> python -V
Python 3.8.3
PS　C:\Users\アカウント名>
```
- ↑のようにPythonのバージョンが表示されたら成功（バージョン番号はインストールする時期により異なります）

## パッケージのインストール

- Pythonには多数のパッケージが存在し、自分の目的に合わせてインストールします
- `Windows PowerShell`を起動し、以下のコマンドを実行
```
PS C:\Users\アカウント名> py -m pip install 【パッケージ名】
```

- Jupyter Labをインストールする場合
```
PS C:\Users\アカウント名> py -m pip install jupyterlab
```

- pipを最新版にする場合
```
PS C:\Users\アカウント名> py -m pip install --upgrade pip
```

## 代表的なパッケージ

|パッケージ名|内容|
|:--|:--|
|`jupyterlab`|Python実行環境ノートブック|
|`matplotlib`|グラフ描画|
|`numpy`|数値計算（`matplotlib`と一緒にインストールされる）|

## パッケージのインストールでエラーが出る場合

Pythonのキャッシュ保存先が、`C:\Users\アカウント名`以下に設定されており、アカウント名が日本語であることが、エラーの原因である場合があります。

- 第2作業エリアに、「Temp」というフォルダを新規作成する（例：`C:\Home\sNNNNNNN\Temp`）
- `Win+S`で検索窓を開き「env」と入力 → システム環境変数の設定を選択
  - 環境変数を選択
  - ユーザ環境変数一覧から「TEMP」を選択 → 編集
  - 変数値をクリックし、ディレクトリの参照 → 先ほど作成したTempフォルダを指定
  - 「TMP」も同様に設定
- アプリを再起動して、再度`pip`コマンドを実行する
