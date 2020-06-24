# PostgreSQL

## 所要時間

- 30分

## インストール

- [PostgreSQL Database Download](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)にいく
- `Windows x86-64`列の一番上にあるバージョン（今回の例では、`12.3`）の`Download`を選択しインストーラーをダウンロード → 起動
- Microsoft Visual C++のインストールが自動的に開始
- インストーラーの手順に従って進める
  - `superuser`のログイン情報に適当な値を入力する
  - `Next`を続ける
  - 最後の画面で「スタックビルダーを起動する」のチェックを外す
- `Finish`

## 環境変数の設定

- ターミナルから`psql`などのコマンドを実行できるように、環境変数を設定します
- `Ctrl+S`で検索窓を開き、`env`と入力 → 「システム環境変数の編集」を選択
- 「システムプロパティ」ウィンドウが開くので、「詳細設定」タブの一番下にある「環境変数」を選択
- 「ユーザの環境変数」パネルの変数一覧から`Path`を選択し、「編集」ボタンをクリック
- Path変数のリストが表示されたら、右パネルから「新規」を選択
- リストに`C:\Program Files\PostgreSQL\12\bin`を入力し、OKをクリック
- `Windows PowerShell`を新規起動し、以下のコマンドを実行してバージョン情報が表示されたら成功

```
PS C:\Users\ユーザ名> psql --version
psql (PostgreSQL) 12.3
```

## サービスの停止と起動

- サービスの停止
  - 管理者権限で`Windows PowerShell`を起動し、以下のコマンドを実行

```
PS C:\Users\ユーザ名> net stop postgresql-x64-12
postgresql-x64-12 サービスを停止中です.
postgresql-x64-12 サービスは正常に停止されました。
```

- サービスの起動
  - 管理者権限で`Windows PowerShell`を起動し、以下のコマンドを実行

```
PS C:\Users\ユーザ名> net start postgresql-x64-12
postgresql-x64-12 サービスを開始します.
postgresql-x64-12 サービスは正常に開始されました。
```

### サービス自動起動の停止（任意）

- 普段は`PostgreSQL`を使用しないので、ログイン時のサービス自動起動を無効にしたい場合は、管理者権限で`Windows PowerShell`を起動し、以下のコマンドを実行

```
PS C:\Users\ユーザ名> sc config postgresql-x64-12 start=demand
[SC] ChangeServiceConfig SUCCESS
```