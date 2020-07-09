# Herokuを使ったウェブアプリのデプロイ

[Heroku](https://jp.heroku.com/)はウェブアプリをホストしてくれるサービスです。ファイルは[ここにあります](./flask/)。

## 所要時間

- 30分

## 前提

- [Flaskを用いたウェブアプリ](webapp-flask.md)

## 手順

### HerokuアカウントとCLIの準備

- [Herokuアカウント](https://signup.heroku.com/signup/dc)の作成
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)のダウンロードとインストール
- `PowerShell`からHerokuにログイン

```
> heroku login
heroku: Press any key to open up the browser to login or q to exit: 
Opening browser to https://cli-auth.heroku.com/auth/cli/browser/a838e0fc-8906-43b8-a12a-9f93243c9839
Logging in... done
Logged in as YOUR_EMAIL_ADDRESS
```

### デプロイに必要なファイルの作成

- `Procfile`

```
web: gunicorn myapp:app --log-file -
```

- `runtime.txt`

```
python-3.8.3

```

- `requirements.txt`の末尾に以下の行を追加

```
gunicorn
```

### `Git`でローカルレポジトリを作成

```
> git init
> git add .
> git commit -m 'Initial commit'
 8 files changed, 246 insertions(+)
 create mode 100644 Procfile
 create mode 100644 README.md
 create mode 100644 myapp.py
 create mode 100644 db.sql
 create mode 100644 requirements.txt
 create mode 100644 runtime.txt
 create mode 100644 templates/index.html
 create mode 100644 templates/layout.html
```

### Herokuアプリの作成

```
> heroku create
Creating app... done, ⬢ calm-escarpment-90498
https://calm-escarpment-90498.herokuapp.com/ | https://git.heroku.com/calm-escarpment-90498.git
```

- PostgreSQLの追加

```
> heroku addons:create heroku-postgresql:hobby-dev
```

- `db.sql`を使ってHeroku上のDBの表作成

```
> heroku pg:psql
--> Connecting to postgresql-adjacent-76040
psql (12.3)
SSL 接続 (プロトコル: TLSv1.2、暗号化方式: ECDHE-RSA-AES256-GCM-SHA384、ビット長: 256、圧縮: オフ)
"help"でヘルプを表示します。

calm-escarpment-90498::DATABASE=> \i db.sql
psql:db.sql:1: NOTICE:  table "papers" does not exist, skipping
DROP TABLE
CREATE TABLE
calm-escarpment-90498::DATABASE=> \q
```

- ローカルレポジトリのHerokuへのアップロード

```
> git push heroku master
```

### Herokuアプリの起動

```
> heroku ps:scale web=1
```

- アプリへのアクセス

```
> heroku open
```

- 開いたページでレコードの追加ができる確認

### Herokuアプリの削除

```
> heroku apps:destory --app APP_NAME
WARNING: This will delete ⬢ calm-escarpment-90498 including all add-ons.
 !    To proceed, type calm-escarpment-90498 or re-run this command with --confirm
 !    calm-escarpment-90498

> calm-escarpment-90498
Destroying ⬢ calm-escarpment-90498 (including all add-ons)... done
```
