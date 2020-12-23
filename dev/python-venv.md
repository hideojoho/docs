# 仮想環境を使ったPython開発

Pythonアプリの開発で、仮想環境を構築する手順。[Solrサーバ](solr-server.md)のクライアント構築を例に。

## 前提

- [Python](pc-python.md)
- [VSCode](pc-vscode.md)
- [Solrサーバ](solr-server.md) (`bin\solr.cmd start -e techproducts`)

## VSCodeの準備

- `Solr`クライアント用フォルダ`solr-client`を[第2作業エリア](pc-workspace.md)に作成
  - `C:\Home\sNNNNNNN\Workspace\solr-client`
- `solr-client`フォルダをVSCodeで開く
- `Solr`クライアント用仮想環境の構築
```
PS C:\Home\sNNNNNNN\Workspace\solr-client> py -m venv venv
```
- 仮想環境の起動
  - :bulb: 仮想環境を起動するとプロンプトの先頭に`(venv)`が表示されます
```
PS C:\Home\sNNNNNNN\Workspace\solr-client> .\venv\Scripts\activate
(venv) PS C:\Home\sNNNNNNN\Workspace\solr-client>
```
- 仮想環境の終了
```
(venv) PS C:\Home\sNNNNNNN\Workspace\solr-client> deactivate
PS C:\Home\sNNNNNNN\Workspace\solr-client>
```

## Pythonモジュールのインストール

:bulb: 仮想環境を利用する利点の1つは、環境ごとに必要なモジュールをインストールするので、
パソコンのOSや他の開発環境に影響を与える危険が少ないことです。一方で、必要なモジュールは
新規環境ごとに構築する必要があります。環境に必要なモジュールは`requirements.txt`に書きます。

- `solr-client`フォルダ内に`requirements.txt`を新規作成し、以下の内容を書き、保存
```
pysolr==3.9.0
urllib3==1.25.10
```
- VSCodeターミナルから以下を実行
```
(venv) PS C:\Home\sNNNNNNN\Workspace\solr-client> py -m pip install -U pip
(venv) PS C:\Home\sNNNNNNN\Workspace\solr-client> py -m pip install -r requirements.txt
```

## Solrクライアントの作成と実行

- `solr-client.py`を新規作成
```python
import pysolr
import urllib3

# Server Information
server_url = 'http://localhost'
server_port = '8983'
server_core = 'techproducts'

# Query (Field:Query_String)
query_field = 'name'
query_string = 'iPod'
query = query_field + ':' + query_string

# Connection
# http://localhost:8983/solr/techproducts/select?q=
solr = pysolr.Solr(
              server_url + ':' + server_port +
              '/solr/' + server_core
              )
# Search and response
results = solr.search(query)

# Print the response
print("Saw {0} result(s).".format(len(results)))
for result in results:
    print("The name is '{0}'.".format(result['name']))

```

- クライアントの実行
```
(venv) PS C:\Home\sNNNNNNN\Workspace\solr-client> python .\solr-client.py
Saw 3 result(s).
The name is 'iPod & iPod Mini USB 2.0 Cable'.
The name is 'Belkin Mobile Power Cord for iPod w/ Dock'. 
The name is 'Apple 60 GB iPod with Video Playback Black'.
```
