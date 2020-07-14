# Lucene + Anserini

- Lucene 8.5.2
- Anserini 0.9.5

## Lucene

### How to use Lucene

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

## URLs

- https://lucene.apache.org/core/8_5_2/demo/overview-summary.html#Indexing_Files
