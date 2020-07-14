# Lucene + Anserini

- Lucene 8.5.2
- Anserini 0.9.5

## How to use Lucene

- Run Lucene to index files in VM but produced index files are stored in a shared folder for later use

```
$ mkdir index
$ docker run -it --rm -v $(pwd)/index:/work/index hideojoho/lucene:8.5.2 /bin/bash -c "java org.apache.lucene.demo.IndexFiles -docs lucene-8.5.2/docs/changes"
cene.demo.IndexFiles -docs lucene-8.5.2/docs/changes"
Indexing to directory 'index'...
adding lucene-8.5.2/docs/changes/ChangesFancyStyle.css
adding lucene-8.5.2/docs/changes/ChangesSimpleStyle.css
adding lucene-8.5.2/docs/changes/ChangesFixedWidthStyle.css
adding lucene-8.5.2/docs/changes/Changes.html
605 total milliseconds
$ ls index/
_0.cfe  _0.cfs  _0.si  segments_1  write.lock
```
- Search with the index files
  - `Ctrl+C` to exit an interactive mode

```
$ docker run -it --rm -v $(pwd)/index:/work/index hideojoho/lucene:8.5.2 /bin/bash -c "java org.apache.lucene.demo.SearchFiles"
Enter query:
style
Searching for: style
1 total matching documents
1. lucene-8.5.2/docs/changes/Changes.html
Press (q)uit or enter number to jump to a page.
q
Enter query:
^C
```

## How to use Anserini

- Download MS Marco Passage Dataset

```
$ mkdir -P collections/msmarco-passage
$ wget https://www.dropbox.com/s/9f54jg2f71ray3b/collectionandqueries.tar.gz -P collections/msmarco-passage
$ tar xvfz collections/msmarco-passage/collectionandqueries.tar.gz -C collections/msmarco-passage
```

- Convert documents into JSON format

```
$ docker run -it --rm -v $(pwd)/collections:/work/collections hideojoho/anserini:0.9.5 /bin/bash -c "python3 anserini/tools/scripts/msmarco/convert_collection_to_jsonl.py --collection-path collections/msmarco-passage/collection.tsv --output-folder collections/msmarco-passage/collection_jsonl"
...
Done!
$ ls collections/msmarco-passage/collection_jsonl
docs00.json  docs01.json  docs02.json  docs03.json  docs04.json  docs05.json  docs06.json  docs07.json  docs08.json
```

- Index the collection

```
docker run -it --rm -v $(pwd)/collections:/work/collections -v $(pwd)/index:/work/index hideojoho/anserini:0.9.5 /bin/bash -c "anserini/target/appassembler/bin/IndexCollection -threads 9 -collection JsonCollection -generator DefaultLuceneDocumentGenerator -input collections/msmarco-passage/collection_jsonl -index index/msmarco-passage/lucene-index-msmarco -storePositions -storeDocvectors -storeRaw"
...
2020-07-14 04:07:14,577 INFO  [main] index.IndexCollection (IndexCollection.java:875) - ============ Final Counter Values ============
2020-07-14 04:07:14,577 INFO  [main] index.IndexCollection (IndexCollection.java:876) - indexed:        8,841,823
2020-07-14 04:07:14,578 INFO  [main] index.IndexCollection (IndexCollection.java:877) - unindexable:            0
2020-07-14 04:07:14,578 INFO  [main] index.IndexCollection (IndexCollection.java:878) - empty:                  0
2020-07-14 04:07:14,578 INFO  [main] index.IndexCollection (IndexCollection.java:879) - skipped:                0
2020-07-14 04:07:14,578 INFO  [main] index.IndexCollection (IndexCollection.java:880) - errors:                 0
2020-07-14 04:07:14,582 INFO  [main] index.IndexCollection (IndexCollection.java:883) - Total 8,841,823 documents indexed in 00:03:20
```

## URLs

- https://lucene.apache.org/core/8_5_2/demo/overview-summary.html#Indexing_Files
- https://github.com/castorini/anserini/blob/master/docs/experiments-msmarco-passage.md
