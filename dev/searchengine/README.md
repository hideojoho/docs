# サーチエンジン開発

情報検索システムの利用方法や開発方法のまとめ。各システムごとに以下の手順を説明します。

- システムのインストールと基本利用
- クライアント開発
  - Web UI
  - チャットボット
- ソースコードの変更とコンパイル
- クラスターへのデプロイ（実験用）

## 環境

- ステップ1-3：研究室PC
- ステップ4: 研究室クラスター

## サーチエンジン機能一覧

:bulb: 厳密な定義ではありません。

|システム|クロール|時系列|索引付け|順位付け|ランク学習|UI|
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
|[Bing](#bing)||||:heavy_check_mark:|||
|[Lucene](#lucene)|||:heavy_check_mark:|:heavy_check_mark:|||
|[Solr](#solr)|||:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:||
|[Elasticsearch](#elasticsearch)||:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:||:heavy_check_mark: (Kibana)|
|[FESS](#fess)|:heavy_check_mark:||:heavy_check_mark:|:heavy_check_mark:||:heavy_check_mark:|
|[Anserini](#anserini)|||:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:||

## Bing Search

Microsoftが提供する商用ウェブ検索サービス。多様なAPIを提供。

- URL: https://docs.microsoft.com/ja-jp/azure/cognitive-services/bing-web-search/

### 手順書

- [システムのインストールと基本利用](bing/1-install.md)
  - [多機能版APIクライアントサーバ](../acs-bingsearch-python.md)
- クライアント開発
  - Web UI
    - [Python](bing/2-client-python.md)
  - チャットボット
    - [Bot Framework](bing/2-client-bot.md)
- 研究室クラスターへのデプロイ
  - [デプロイ](bing/3-k8s.md)
  - [Jupyter Notebookからのアクセス](../k8s/ipynb/bingsearch.ipynb)

## Lucene

Solr / Elasticsearch / FESS / Anserini に基本機能を提供している根幹システム。

- URL: https://lucene.apache.org/

### 手順書

- [システムのインストールと基本利用](lucene/1-install.md)
- [ソースファイルのコンパイル](lucene/3-compile.md)
- 研究室クラスターでの開発
  - [ソースファイルのコンパイル](lucene/3-compile-k8s.md)

## Solr

Luceneをベースにした検索システム。「文書」検索が得意。ランク学習機能がある。

- URL: https://lucene.apache.org/

## Elasticsearch

Luceneをベースにした検索システム。時系列データの扱いが得意。多機能データ解析UIの[Kibana](https://www.elastic.co/jp/kibana/)と連携できる。

- URL: https://www.elastic.co/jp/elasticsearch/

### 手順書

- [システムのインストールと基本利用](elasticsearch/1-install.md)

## FESS

Elasticsearchをベースにした検索システム。クローラーや検索UIを搭載しているのが特徴。

- https://fess.codelibs.org/ja/

## Anserini

Luceneをベースにした検索システム。研究用データセットの処理が得意。[Pyserini](https://github.com/castorini/pyserini)というPython用ラッパーもある。

- URL: https://github.com/castorini/anserini
