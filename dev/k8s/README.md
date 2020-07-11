# 研究室クラスターの使い方

## 前提

- GitHubアカウント + 研究室組織アカウントへの追加
- Python
- VSCodo + Pythonプラグイン

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

### VSCode経由で使用する場合
- URLの`/lab'の部分を`/tree`に変更
- 画面右上の「Control Panel」を選択
- 画面上部メニューから「Token」を選択
- `Request My New Token`を選択し、表示されたトークンをコピペする
  - :warning: 本トークンは一度しか表示されない
  - 必要になったら新しいトークンを発行する
- VSCodeを起動する
  - `Ctrl+Shift+P` → `notebook`と入力し、`Python: Create New Blank Jupyter Notebook`を選択
  - Notebookの画面が表示されたら、`Ctrl+Shift+P` → `remote`と入力し、`Python: Specify local or remote Jupyter servers for connection`を選択
