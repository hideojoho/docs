# 卒論・修論用AsciiDoctorテンプレート

## VSCodeの設定

- AsciiDoctorの拡張機能をインストール
- VSCodeの設定
  - AsciiDocの設定画面で `Asciidoc: Asciidoctorpdf_command`に以下を設定
    ```
    asciidoctor-pdf -r asciidoctor-pdf-cjk-kai_gen_gothic -a pdf-stylesdir=themes -a pdf-style=custom-theme.yml
    ```
  - `Asciidoc: Use_asciidoctorpdf` の `use asciidoctor-pdf...` にチェック

## ファイル一覧

- PDF出力サンプル：[index.pdf](index.pdf)

### 設定ファイル
- 全体の設定：[index.adoc](index.adoc)
- スタイル設定：[custom-theme.yml](themes/custom-theme.yml)

### 抄録
- 抄録：[abstact.adoc](abstract.adoc)

### 本文
- 序論：[introduction.adoc](introduction.adoc)
- 方法：[methods.adoc](methods.adoc)
- 結果：[results.adoc](results.adoc)
- 議論：[discussion.adoc](discussion.adoc)
- 結論：[conclusion.adoc](conclusion.adoc)

### 引用文献・付録
- 引用文献：[reference.adoc](reference.adoc)
- 付録：[appendix.adoc](appendix.adoc)



