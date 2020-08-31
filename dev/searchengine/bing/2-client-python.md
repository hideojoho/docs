# Bing Web検索のUIクライアント（Pythonウェブアプリ）

## 準備

- [APIクライアントサーバの構築](1-install.md)
  - http://localhost:5000/
```
{
  "status": "Ready"
}
```

## 仮想環境の構築

- [仮想環境を使ったPython開発](../../python-venv.md)の手順に従う
- `bing-search-ui`という仮想環境を構築
- `requirements.txt`を新規作成
```
flask
```
- Pythonモジュールをインストール

## UIクライアント

### フォルダ構成

```
bing-search-ui/
  ├ app.py
  └ templates/
      ├ form.html
      ├ index.html
      ├ layout.html
      ├ result.html
      └ serp.html
```

- `app.py`
  
```
import urllib.request
import json
from flask import *
app = Flask(__name__)

app_name = "Bing Web検索 UI"
app_port = 5001
bing_search_url = "http://localhost:5000"

@app.route("/", methods=['GET'])
def index():
  query = request.args.get('q', default=None, type=str)
  if query:
    results = bing_search(query)
    return render_template('result.html', title=app_name, query=query, results=results)
  else:
    return render_template('index.html', title=app_name)

def bing_search(query):
  params = {
    'q': query
  }
  req = urllib.request.Request('{}?{}'.format(bing_search_url, urllib.parse.urlencode(params)))
  with urllib.request.urlopen(req) as res:
    results = json.loads(res.read().decode('utf8'))
  return results

if __name__ == "__main__":
    app.run(debug=True, port=app_port)
```

- `layout.html`
  
```
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <title>{{ title }}</title>
  </head>
  <body>
    <h1>{{ title }}</h1>
    {% block content %}{% endblock %}
  </body>
</html>
```

- `index.html`

```
{% extends "layout.html" %}
{% block content %}
{% include "form.html" %}
{% endblock %}
```

- `form.html`

```
<form action="/" method="GET">
  <input type="search" name="q" placeholder="キーワードを入力" value="{{ query }}"> <input type="submit">
</form>
```

- `result.html`

```
{% extends "layout.html" %}
{% block content %}
{% with query = query, results = results %} 
  {% include "form.html" %}
  {% include "serp.html" %}
{% endwith %}
{% endblock %}
```

- `serp.html`

```
{% for doc in results.response %}
<p>
  <a href="{{ doc.url }}">{{ doc.title }}</a>
  <br/>
  {{ doc.snippet }}
  <br/>
  <a href="{{ doc.url }}" style="font-size:small;color:gray">{{ doc.url }}</a>
</p>
{% endfor %}
```

### クライアントの実行

```
(bing-search-ui) PS C:\Home\sNNNNNNN\Workspace\venv\bing-search-ui> py .\app.py
```

### Web UI

- http://localhost:5001
  

## 発展のアイディア

- `templates`フォルダ以下のhtmlファイルを編集して、Web UIの見た目を変えたり、Javascriptを使って動的な機能を導入する
- [多機能版APIクライアントサーバ](../../acs-bingsearch-python.md)に切り替えて、UIからカテゴリー別検索ができるようにする

## URLs

- https://flask.palletsprojects.com/en/1.1.x/
- https://jinja.palletsprojects.com/en/2.11.x/