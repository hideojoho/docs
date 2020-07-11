# 研究室クラスターの使い方

## 前提

- GitHubアカウント + 研究室組織アカウントへの追加
- [Python](../pc-python.md)
- [VSCodo](../pc-vscode.md) + Pythonプラグイン

## 基本事項

- 研究室クラスターには、クラスター上で動いている`JupyterHub`を経由してアクセスします
- 研究室のJupyterHubのNotebookは、以下の二通りでアクセスできます
  - ブラウザ経由
  - VSCode経由（おすすめ）

## Jupyter Notebookの準備

### ブラウザ経由で使用する場合
- http://isr2.slis.tsukuba.ac.jp にアクセス
  - 学外からのアクセスの場合は、VPN接続が必要です
- 自分のGitHubアカウントで認証
  - ログインできない場合は、アカウントがwhitelistに追加されていない可能性がありますので、指導教員に連絡してください
- Server Optionsから適したNotebookを選択
  - 初めは一番上の`Minimal environment`で大丈夫です

### VSCode経由で使用する場合
- URLの`/lab`の部分を`/tree`に変更
- 画面右上の「Control Panel」を選択
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
    - `http://isr2.slis.tsukuba.ac.jp/user/[github username]/?token=[token]`
    - `[github username]`: 自分のGitHubアカウント名
    - `[token]`: ↑で入手したtoken
  - 画面右下に表示される`Reload`ボタンを選択 → 左パネルからNotebookを選択
  - 先ほど作成だけしておいたセルを実行する
    - Notebookアイコンメニューの右端の`Jupyter Server`が接続されたアイコンになりURLの一部が表示されていたら、接続が成功しています
- これ以降、Jupyterサーバとの接続が切れるまでは、VSCode上のプログラムは研究室クラスターのJupyterサーバ上で処理されて、その結果がVSCode上に表示されます
  - プログラムは手元の研究室PCにありますが、入出力データは研究室クラスター内にしか存在していないので、注意してください
  
 
 ## Jupyter Notebook コードスニペット集
 
 
  
