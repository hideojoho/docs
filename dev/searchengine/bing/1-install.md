# Bing Web検索のインストールと基本利用

## 前提

- [Azureリソースの取得](../../acs-resource.md)
- 作成したBing Web検索用リソースの左パネルから「キーとエンドポイント」を選択
- 「キー1」と「エンドポイント」をコピペできるようにしておく

## 仮想環境の構築

- [仮想環境を使ったPython開発](../../python-venv.md)の手順に従う
- `bing-search`という仮想環境を構築
- `requirements.txt`を新規作成
```
azure-cognitiveservices-search-websearch
```
- Pythonモジュールをインストール

## APIクライアントの作成

- `bingwebsearch.py`を新規作成
  - `YOUR_SUBSCRIPTION_KEY`：作成したリソースの「キー１」
  - `YOUR_ENDPOINT`：作成したリソースの「エンドポイント」

```
# Import required modules.
from azure.cognitiveservices.search.websearch import WebSearchClient
from azure.cognitiveservices.search.websearch.models import SafeSearch
from msrest.authentication import CognitiveServicesCredentials

# Replace with your subscription key and endpoint
KEY = "YOUR_SUBSCRIPTION_KEY"
EP = "YOUR_ENDPOINT"

# Instantiate the client and replace with your endpoint.
client = WebSearchClient(endpoint="EP", credentials=CognitiveServicesCredentials(KEY))

# Make a request. Replace Yosemite if you'd like.
QUERY = "Yosemite"
web_data = client.web.search(query=QUERY)
print("Searched for Query: \"" + QUERY + "\"")

if hasattr(web_data.web_pages, 'value'):
    first_web_page = web_data.web_pages.value[0]
    print("First web page name: {} ".format(first_web_page.name))
    print("First web page URL: {} ".format(first_web_page.url))
else:
    print("Didn't find any web pages...")
```

## APIクライアントの実行

:bulb: 検索結果は異なる可能性があります

```
(bing-search) PS C:\Home\sNNNNNNN\Workspace\venv\bing-search> py .\bingwebsearch.py
Searched for Query: "Yosemite"
First web page name: Yosemite National Park (U.S. National Park Service) 
First web page URL: https://www.nps.gov/yose/index.htm
```

## APIクライアントサーバの構築

検索UIからアクセスするためのAPIクライアントサーバ

```
検索UI <--> APIクライアントサーバ <--> Bing検索
```


- `requirements.txt`に以下を追加し、モジュールをインストール

```
flask
```

- `bingwebsearch-app.py`を新規作成

```
# Import required modules.
from azure.cognitiveservices.search.websearch import WebSearchClient
from azure.cognitiveservices.search.websearch.models import SafeSearch
from msrest.authentication import CognitiveServicesCredentials
from flask import *

app = Flask(__name__)

# Replace with your subscription key and endpoint
KEY = "YOUR_SUBSCRIPTION_KEY"
EP = "YOUR_ENDPOINT"

# Instantiate the client and replace with your endpoint.
client = WebSearchClient(endpoint="EP", credentials=CognitiveServicesCredentials(KEY))

@app.route("/", methods=['GET'])
def index():
    q = request.args.get('q', default=None, type=str)

    if q:
        web_data = client.web.search(query=q)
        if hasattr(web_data.web_pages, 'value'):
            response = []
            for i in range(len(web_data.web_pages.value)):
                page = {
                    "title": web_data.web_pages.value[i].name,
                    "url": web_data.web_pages.value[i].url,
                    "snippet": web_data.web_pages.value[i].snippet
                }
                response.append(page)
            return {
                "response": response
            }
        else:
            return {
                "response": None
            }
    else:
        return {
            "Status": "Ready"
        }

if __name__ == "__main__":
    app.run(debug=True)
```

## APIクライアントサーバの実行

```
 (bing-search) PS C:\Home\sNNNNNNN\Workspace\venv\bing-search> py .\bingwebsearch-app.py
 * Serving Flask app "bingwebsearch-app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 119-761-731
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## APIクライアントサーバのテスト

- http://127.0.0.1:5000/

```
{
  "Status": "Ready"
}
```

- http://127.0.0.1:5000/?q=yosemite

```
{
  "response": [
    {
      "snippet": "Yosemite Not just a great valley, but a shrine to human foresight, the strength of granite, the power of glaciers, the persistence of life, and the tranquility of the High Sierra. First protected in 1864, Yosemite National Park is best known for its waterfalls, but within its nearly 1,200 square miles, you can find deep valleys, grand meadows ...", 
      "title": "Yosemite National Park (U.S. National Park Service)", 
      "url": "https://www.nps.gov/yose/index.htm"
    }, 
    {
      "snippet": "Yosemite National Park in Mariposa County is home to majestic attractions and premier lodging. A must see for any trip to California. Plan your vacation to Yosemite today! Discover things to do in Yosemite, places to stay in Yosemite and some of the best places to eat in Yosemite Mariposa County.", 
      "title": "Yosemite National Park | Lodging, Camping, Attractions ...", 
      "url": "https://www.yosemite.com/"
    }, 
    {
      "snippet": "Yosemite National Park (/ j o\u028a \u02c8 s \u025b m \u026a t i / yoh-SEM-i-tee) is an American national park located in the western Sierra Nevada of Central California, bounded on the southeast by Sierra National Forest and on the northwest by Stanislaus National Forest.The park is managed by the National Park Service and covers an area of 748,436 acres (1,169 sq mi; 3,029 km 2) and sits in four counties ...", 
      "title": "Yosemite National Park - Wikipedia", 
      "url": "https://en.wikipedia.org/wiki/Yosemite_National_Park"
    }, 
    ...
  ]
}
```

- http://127.0.0.1:5000/?q=querythatshouldnothaveanyresultsfortestingpurposebutyouwillrealisethisisverychallenging

```
{
  "response": null
}
```

## 多機能版APIクライアントサーバ

- [多機能版APIクライアントサーバ](../../acs-bingsearch-python.md)

## URLs

- [Bing Search APIのドキュメント](https://docs.microsoft.com/ja-jp/azure/cognitive-services/bing-web-search/)
