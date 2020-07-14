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
$ ls index/msmarco-passage/lucene-index-msmarco/
_0.fdt             _1_Lucene50_0.doc  _3.fnm             _4_Lucene50_0.tim  _6.nvm             _7_Lucene80_0.dvd
_0.fdx             _1_Lucene50_0.pos  _3.nvd             _4_Lucene50_0.tip  _6.si              _7_Lucene80_0.dvm
_0.fnm             _1_Lucene50_0.tim  _3.nvm             _4_Lucene80_0.dvd  _6.tvd             _8.fdt
_0.nvd             _1_Lucene50_0.tip  _3.si              _4_Lucene80_0.dvm  _6.tvx             _8.fdx
_0.nvm             _1_Lucene80_0.dvd  _3.tvd             _5.fdt             _6_Lucene50_0.doc  _8.fnm
_0.si              _1_Lucene80_0.dvm  _3.tvx             _5.fdx             _6_Lucene50_0.pos  _8.nvd
_0.tvd             _2.fdt             _3_Lucene50_0.doc  _5.fnm             _6_Lucene50_0.tim  _8.nvm
_0.tvx             _2.fdx             _3_Lucene50_0.pos  _5.nvd             _6_Lucene50_0.tip  _8.si
_0_Lucene50_0.doc  _2.fnm             _3_Lucene50_0.tim  _5.nvm             _6_Lucene80_0.dvd  _8.tvd
_0_Lucene50_0.pos  _2.nvd             _3_Lucene50_0.tip  _5.si              _6_Lucene80_0.dvm  _8.tvx
_0_Lucene50_0.tim  _2.nvm             _3_Lucene80_0.dvd  _5.tvd             _7.fdt             _8_Lucene50_0.doc
_0_Lucene50_0.tip  _2.si              _3_Lucene80_0.dvm  _5.tvx             _7.fdx             _8_Lucene50_0.pos
_0_Lucene80_0.dvd  _2.tvd             _4.fdt             _5_Lucene50_0.doc  _7.fnm             _8_Lucene50_0.tim
_0_Lucene80_0.dvm  _2.tvx             _4.fdx             _5_Lucene50_0.pos  _7.nvd             _8_Lucene50_0.tip
_1.fdt             _2_Lucene50_0.doc  _4.fnm             _5_Lucene50_0.tim  _7.nvm             _8_Lucene80_0.dvd
_1.fdx             _2_Lucene50_0.pos  _4.nvd             _5_Lucene50_0.tip  _7.si              _8_Lucene80_0.dvm
_1.fnm             _2_Lucene50_0.tim  _4.nvm             _5_Lucene80_0.dvd  _7.tvd             segments_1
_1.nvd             _2_Lucene50_0.tip  _4.si              _5_Lucene80_0.dvm  _7.tvx             write.lock
_1.nvm             _2_Lucene80_0.dvd  _4.tvd             _6.fdt             _7_Lucene50_0.doc
_1.si              _2_Lucene80_0.dvm  _4.tvx             _6.fdx             _7_Lucene50_0.pos
_1.tvd             _3.fdt             _4_Lucene50_0.doc  _6.fnm             _7_Lucene50_0.tim
_1.tvx             _3.fdx             _4_Lucene50_0.pos  _6.nvd             _7_Lucene50_0.tip
```

- Sample queries

```
$ docker run -it --rm -v $(pwd)/collections:/work/collections -v $(pwd)/index:/work/index hideojoho/anserini:0.9.5 /bin/bash -c "python3 anserini/tools/scripts/msmarco/filter_queries.py  --qrels collections/msmarco-passage/qrels.dev.small.tsv --queries collections/msmarco-passage/queries.dev.tsv --output collections/msmarco-passage/queries.dev.small.tsv"
Done!
$ wc -l collections/msmarco-passage/queries.dev.small.tsv
6980 collections/msmarco-passage/queries.dev.small.tsv
```

- Perform a search with BM25

```
$ mkdir runs
$ docker run -it --rm -v $(pwd)/collections:/work/collections -v $(pwd)/index:/work/index -v $(pwd)/runs:/work/runs hideojoho/anserini:0.9.5 /bin/bash -c "anserini/target/appassembler/bin/SearchMsmarco -hits 1000 -threads 1 -index index/msmarco-passage/lucene-index-msmarco -queries collections/msmarco-passage/queries.dev.small.tsv -output runs/run.msmarco-passage.dev.small.tsv"
Initializing BM25, setting k1=0.82 and b=0.68
Retrieving query 0 (0.436 s/query)
Retrieving query 100 (0.101 s/query)
...
Retrieving query 6900 (0.063 s/query)
Total retrieval time: 438.604 s
Done!
```

- Evaluate the performance of search results

```
$ docker run -it --rm -v $(pwd)/collections:/work/collections -v $(pwd)/index:/work/index -v $(pwd)/runs:/work/runs hideojoho/anserini:0.9.5 /bin/bash -c "python3 anserini/tools/scripts/msmarco/msmarco_eval.py collections/msmarco-passage/qrels.dev.small.tsv runs/run.msmarco-passage.dev.small.tsv"
#####################
MRR @10: 0.18741227770955546
QueriesRanked: 6980
#####################
```


## URLs

- https://lucene.apache.org/core/8_5_2/demo/overview-summary.html#Indexing_Files
- https://github.com/castorini/anserini/blob/master/docs/experiments-msmarco-passage.md
