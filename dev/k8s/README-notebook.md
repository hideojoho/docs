
# 研究室クラスターNotebookの使い方

## 前提

- GitHubアカウント + 研究室組織アカウントへの追加
- [Python](../pc-python.md)
- [VSCodo](../pc-vscode.md) + Pythonプラグイン

## 基本事項

- 研究室クラスターには、クラスター上で動いている`JupyterHub`を経由してアクセスします
- 研究室のJupyterHubのNotebookは、以下の二通りでアクセスできます
  - ブラウザ経由
  - VSCode経由（おすすめ）

## ブラウザ経由で使用する場合
- [JupyterHubログインページ](http://isr.slis.tsukuba.ac.jp/jupyter/) にアクセス（要パスワード）
  - 学外からのアクセスの場合は、VPN接続が必要です
- 自分のGitHubアカウントで認証
  - ログインできない場合は、アカウントがwhitelistに追加されていない可能性がありますので、指導教員に連絡してください
- Server Optionsから適したNotebookを選択
  - 初めは一番上の`jupyter/minimal-notebook`を選択しましょう

## VSCode経由で使用する場合
- 「ブラウザ経由で使用する場合」の手順を実行し、Notebookを起動しておく
- 画面上部メニュー「File」→「Hub Control Panel」を選択
- 画面上部メニューから「Token」を選択
- `Request My New Token`を選択し、表示されたトークンをコピペする
  - :warning: 本トークンは一度しか表示されないので注意
  - 必要になったら新しいトークンを発行して大丈夫です
- トークンをコピペしたら、上部メニューから`Home` → `My Server`を選択し、Jupyter Labを起動しておく
- VSCodeを起動する
  - Jupyter Notebookを保存するフォルダを作成しておく
  - 「ファイル」→「フォルダを開く」で作成したフォルダを選択
  - `Ctrl+Shift+P` → `notebook`と入力し、`Python: Create New Blank Jupyter Notebook`を選択
  - Notebookの画面が表示されたら、最初のセルに以下のコマンドを入力し、Notebookを名前を付けて保存する（セルの実行はしない）
    - `print('Hello')`
  - `Ctrl+Shift+P` → `remote`と入力し、`Python: Specify local or remote Jupyter servers for connection`を選択
  - `Existing`を選択し、表示された入力欄に以下のURLを入力
    - `http://isr.slis.tsukuba.ac.jp/jupyter/user/[github username]/?token=[token]`
    - `[github username]`: 自分のGitHubアカウント名
    - `[token]`: ↑で入手したtoken
  - 画面右下に表示される`Reload`ボタンを選択 → 左パネルからNotebookを選択
  - 先ほど作成だけしておいたセルを実行する
    - Notebookアイコンメニューの右端の`Jupyter Server`が接続されたアイコンになりURLの一部が表示されていたら、接続が成功しています
- これ以降、Jupyterサーバとの接続が切れるまでは、VSCode上のプログラムは研究室クラスターのJupyterサーバ上で処理されて、その結果がVSCode上に表示されます
  - プログラムは手元の研究室PCにありますが、入出力データは研究室クラスター内にしか存在していないので、注意してください
- `Error: Cannot execute code, session has been disposed.`等のメッセージが表示されたら、Jupyerサーバとの接続が切断されていますので、新しいトークンを取得するところから再開しましょう。
 
## 接続出来たら

必ず[研究室クラスターのファイルやデータについて](README-data.md)を読んで、指示に従ってください。

## Notebookの終了方法

:bulb: 人間が寝ている間にコンピュータに仕事をさせるのは良い習慣です。それ以外の場合は、一日の終わりにNotebookを終了する習慣をつけてください。そうすることで、他のメンバーが使用されていないクラスター資源を活用できます。

- ファイルやデータが[永続保存場所](README-data.md)にあることを確認する
- VSCodeのJupyer Notebookを閉じる
  - 自動的に研究室サーバとの接続が解除される
- [JupyterHubホーム画面](http://isr.slis.tsukuba.ac.jp/jupyter/home)から`Stop My Server`を選択
  - この時点で[永続保存場所](README-data.md)以外の一時ファイルは消えると考えてください
  - サーバ停止するまでしばらく時間がかかります
  - 右上から`Logout`を選択
