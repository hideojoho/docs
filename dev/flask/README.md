# Flask + PostgreSQL + Heroku

## Requirements

- Python
- PostgreSQL
  
## DB Setup

- Create a db `myapp_db`

```
> psql -h localhost -p 5432 -U postgres -d postgres
postgres=# create database myapp_db;
...
postgres=# \q
```

- Create tables in `myapp_db` using `db.sql`

```
> psql -h localhost -p 5432 -U postgres -d myapp_db
リレーションが見つかりませんでした。
myapp_db=# \i db.sql
psql:db.sql:1: NOTICE:  テーブル"papers"は存在しません、スキップします
DROP TABLE
CREATE TABLE

myapp_db=#
```

- Check the table and its columns

```
myapp_db=# \dt
            リレーション一覧
 スキーマ |  名前  |    型    |  所有者
----------+--------+----------+----------
 public   | papers | テーブル | postgres
(1 行)


myapp_db=# \d papers
                                       テーブル"public.papers"
       列        |        型         | 照合順序 | Null 値を許容 |             デフォルト
-----------------+-------------------+----------+---------------+------------------------------------
 id              | integer           |          | not null      | nextval('papers_id_seq'::regclass)
 title           | character varying |          |               |
 author          | character varying |          |               |
 citation_number | integer           |          |               |
インデックス:
    "papers_pkey" PRIMARY KEY, btree (id)


myapp_db=# \q
```

## Install Python packages

- Create a file `requirements.txt`

```
flask
sqlalchemy
psycopg2
```

- Install the packages

```
> py -m pip install -r requirements.txt
```

## Local deploy

- Set an environmental variable `DATABASE_URL` in `PowerShell`

```
> Set-Item Env:DATABASE_URL -value 'postgres://postgres:[password for postgres]@localhost:5432/myapp_db'
```

- Start the app

```
> python myapp.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 160-151-035
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

- Go to http://localhost:5000 and see if you can add a record

## Deply to Heroku

- Create an account of Heroku
- Install Heroku CLI
- Login to Heroku from `PowerShell`

```
> heroku login
heroku: Press any key to open up the browser to login or q to exit: 
Opening browser to https://cli-auth.heroku.com/auth/cli/browser/a838e0fc-8906-43b8-a12a-9f93243c9839
Logging in... done
Logged in as YOUR_EMAIL_ADDRESS
```

- Create a file `Procfile`

```
web: gunicorn myapp:app --log-file -
```

- Create a file `runtime.txt`

```
python-3.8.3

```

- Add the line to `requirements.txt`

```
gunicorn
```

- Run some git commands

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

- Create a Heroku app

```
> heroku create
Creating app... done, ⬢ calm-escarpment-90498
https://calm-escarpment-90498.herokuapp.com/ | https://git.heroku.com/calm-escarpment-90498.git
```

- Add PostgreSQL Addon to the app

```
> heroku addons:create heroku-postgresql:hobby-dev
```

- Import SQL to Heroku DB

```
> heroku pg:psql
--> Connecting to postgresql-adjacent-76040
psql (11.2, server 12.3 (Ubuntu 12.3-1.pgdg16.04+1))
WARNING: psql major version 11, server major version 12.
         Some psql features might not work.
SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
Type "help" for help.

calm-escarpment-90498::DATABASE=> \i db.sql
psql:db.sql:1: NOTICE:  table "papers" does not exist, skipping
DROP TABLE
CREATE TABLE
calm-escarpment-90498::DATABASE=> \q
```

- Push the local contents to Heroku repository

```
> git push heroku master
```

- Start the app

```
> heroku ps:scale web=1
```

- Open Heroku App

```
> heroku open
```

- Check if you can add a record

## Delete Heroku App

```
> heroku apps:destory
WARNING: This will delete ⬢ calm-escarpment-90498 including all add-ons.
 !    To proceed, type calm-escarpment-90498 or re-run this command with --confirm
 !    calm-escarpment-90498

> calm-escarpment-90498
Destroying ⬢ calm-escarpment-90498 (including all add-ons)... done
```