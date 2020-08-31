# Bing検索（Python SDK）

```
検索UI <--> APIクライアントサーバ <--> Bing検索
```

## APIクライアントサーバ

パラメータ
- `q`: クエリ
- `ct`: カテゴリ
  - `web`: Web検索
  - `image`: 画像検索
  - `news`: ニュース検索
  - `video`: 動画検索

```
# Import required modules.
from azure.cognitiveservices.search.websearch import WebSearchClient
from azure.cognitiveservices.search.imagesearch import ImageSearchClient
from azure.cognitiveservices.search.newssearch import NewsSearchClient
from azure.cognitiveservices.search.videosearch import VideoSearchClient
from azure.cognitiveservices.search.videosearch.models import VideoPricing, VideoLength, VideoResolution, VideoInsightModule
from azure.cognitiveservices.search.websearch.models import SafeSearch
from msrest.authentication import CognitiveServicesCredentials
from flask import *

app = Flask(__name__)

# Replace with your subscription key and endpoint
KEY = "YOUR_SUBSCRIPTION_KEY"
EP = "YOUR_ENDPOINT"

@app.route("/", methods=['GET'])
def index():
    response = []
    q = request.args.get('q', default=None, type=str)
    if not q:
        return { "response": response }

    ct = request.args.get('ct', default='web', type=str)
    if ct == 'web':
        client = WebSearchClient(endpoint=EP,
                        credentials=CognitiveServicesCredentials(KEY))
        result = client.web.search(query=q)
        if hasattr(result.web_pages, 'value'):
            for i in range(len(result.web_pages.value)):
                page = {
                    "title": result.web_pages.value[i].name,
                    "url": result.web_pages.value[i].url,
                    "snippet": result.web_pages.value[i].snippet
                }
                response.append(page)
    if ct == 'image':
        client = ImageSearchClient(endpoint=EP,
                        credentials=CognitiveServicesCredentials(KEY))
        result = client.images.search(query=q)
        if hasattr(result, 'value'):
            for i in range(len(result.value)):
                page = {
                    "content_url": result.value[i].content_url
                }
                response.append(page)
    if ct == 'news':
        client = NewsSearchClient(endpoint=EP,
                        credentials=CognitiveServicesCredentials(KEY))
        result = client.news.search(query=q)
        if hasattr(result, 'value'):
            for i in range(len(result.value)):
                page = {
                    "title": result.value[i].name,
                    "url": result.value[i].url,
                    "description": result.value[i].description
                }
                response.append(page)
    if ct == 'video':
        client = VideoSearchClient(endpoint=EP,
                        credentials=CognitiveServicesCredentials(KEY))
        result = client.videos.search(query=q)
        if hasattr(result, 'value'):
            for i in range(len(result.value)):
                page = {
                    "title": result.value[i].name,
                    "content_url": result.value[i].content_url
                }
                response.append(page)

    return {
        "response": response
    }

if __name__ == "__main__":
    app.run(debug=True)
```
