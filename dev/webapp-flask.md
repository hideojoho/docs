# Flaskを使ったウェブアプリ開発

PythonのFlaskフレームワークを用いたウェブアプリの開発。データベースにはPostgreSQLを使います。ファイルは[ここにあります](./flask/)。

## 所要時間

- 30分

## 前提

- [Gitのインストール](pc-git.md)
- [Pythonのインストール](pc-python.md)
- [PostgreSQLのインストール](pc-postgresql.md)

## 手順

- ローカルデータベースの作成
- Pythonパッケージのインストール
- アプリの作成
- ローカル環境でのデプロイ

### ローカルデータベースの作成

- データベース `myapp_db` の作成

```
> psql -h localhost -p 5432 -U postgres -d postgres
postgres=# create database myapp_db;
...
postgres=# \q
```

- `db.sql` を用いて表 `myapp_db` を作成

```
> psql -h localhost -p 5432 -U postgres -d myapp_db
リレーションが見つかりませんでした。
myapp_db=# \i db.sql
psql:db.sql:1: NOTICE:  テーブル"papers"は存在しません、スキップします
DROP TABLE
CREATE TABLE

myapp_db=#
```

- 表の確認

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

### Pythonパッケージのインストール

- ファイル `requirements.txt` の新規作成

```
flask
sqlalchemy
psycopg2
```

- パッケージのインストール

```
> py -m pip install -r requirements.txt
```

### アプリの作成

```Python
import os
from flask import Flask, render_template, request, redirect, url_for

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.secret_key = b'random string...'

Base = declarative_base()

Engine = create_engine(os.environ.get('DATABASE_URL'))
Session = sessionmaker(bind=Engine)

class Paper(Base):
    __tablename__ = 'papers'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    author = Column(String(255))
    citation_number = Column(Integer())

    def to_dict(self):
        return {
            'id': int(self.id),
            'title': str(self.title),
            'author': str(self.author),
            'citation_number': int(self.citation_number)
        }


@app.route('/', methods=['GET'])
def index():
    ses = Session()
    data = ses.query(Paper).all()
    ses.close()
    return render_template(
        'index.html',
        title='Papers',
        data=data
    )


@app.route('/add', methods=['POST'])
def add_record():
    title = request.form.get('title')
    author = request.form.get('author')
    citation_number = request.form.get('citation_number')
    new_paper = Paper(title=title, author=author,
                      citation_number=citation_number)
    ses = Session()
    ses.add(new_paper)
    ses.commit()
    ses.close()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run()
```

### ローカル環境でのデプロイ

- `PowerShell`で環境変数 `DATABASE_URL`の設定
  - `[password for postgres]`はPostgreSQLのインストール時に設定したパスワード

```
> Set-Item Env:DATABASE_URL -value 'postgres://postgres:[password for postgres]@localhost:5432/myapp_db'
```

- アプリの開始

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

- http://localhost:5000 に行き、新規レコードの追加を確認

### 次：Herokuへのデプロイ

- [Herokuへのデプロイ](heroku-pc.md)
