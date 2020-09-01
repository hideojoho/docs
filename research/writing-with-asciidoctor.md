#  Asciidoctorを使った論文執筆（卒論・修論）

:bulb: `Asciidoctor`は`Markdown`の高機能版のような文書作成環境

## Asciidoctorのインストール

- [Rubyをインストール](../dev/pc-ruby.md)する
-  `Windows Powershell`を起動し、以下のコマンドを実行
```
PS C:\Users\アカウント名>gem install asciidoctor asciidoctor-diagram asciidoctor-pdf-cjk-kai_gen_gothic
PS C:\Users\アカウント名>asciidoctor-pdf-cjk-kai_gen_gothic-install
```

## 作業用フォルダの作成

- [ファイルやデータの整理](files-and-data.md)を参考に、`Thesis`フォルダを作成
- `Thesis`フォルダの下に、`ver1`フォルダを作成
- [卒論・修論用AsciiDoctorテンプレート](../templates/asciidoctor-thesis)からファイルをコピーして、`ver1`に保存
- 以下のようなファイル構成になっていることを確認

### ファイル構成例

```
C:
  ├ Users
    ├ アカウント名
      ├ SynologyDrive
        ├ ...
        ├ MyFolders
          ├ ...
          ├ Thesis # 学位論文の原稿
           ├ ver1
             ├ abstract.adoc
             ├ index.adoc
             ├ introduction.adoc
             ├ ...
             ├ reference.adoc
             └ themes
               └ custom-theme.yml
```

## VSCodeでの執筆

- これ以降はVSCodeで編集
- `ver1`をVSCodeで開く（フォルダを右クリック > Codeで開く）
- [Asciidoctor用の拡張機能をインストール](../dev/pc-vscode.md)
- `index.adoc`を開いて、画面右上のプレビューアイコンを選択
- 右ペインに文書のプレビューが表示されることを確認

### 文書設定の変更

- `index.adoc`の以下の部分を適宜
```
= 論文題目
// Settings to change 変更する設定
:author: 著者名
:revnumber: 1.0 // 版番号
:revdate: 2020-01-01 // 作成日時
:revremark: この版の簡単な説明
```
- 目次の表示設定
```
// 目次を表示
toc::[]

// 目次を非表示
// toc::[]
```

### PDFへの出力

- `Ctrl+Shift+P`キーでVSCodeのコマンドパレットを表示
- `AsciiDoc: Export document as PDF`を選択
- `This feature requires wkhtmltopdf do you want to download`というメッセージが画面右下に表示されたら`Download`を選択
- 保存先の選択
- PDFファイルが生成されたことを確認

### 章ファイルのインポート

- テンプレートをダウンロードした段階では、以下のファイルのみがインポートされる設定になっている
  - 抄録：`abstract.adoc`
  - 序論：`introduction.adoc`
  - 引用文献：`reference.adoc`
- 他の章をインポートする場合は、`index.adoc`の設定を以下のように変更する（方法の章の例）
```
// 方法の章の非インポート
// include::methods.adoc[]

// 方法の章のインポート
include::methods.adoc[]
```

## 原稿の執筆

### 各章のファイル名

:bulb: 章の構成は以下を基本としつつも、必要に応じて変更してもよい

- 抄録：`abstract.adoc`
- 序論：`introduction.adoc`
- 方法：`methods.adoc`
- 結果：`results.adoc`
- 議論：`discussion.adoc`
- 結論：`conclusion.adoc`
- 引用文献：`reference.adoc`
- 付録：`appendix.adoc`（任意）

### 章・図表・コード・引用文献の参照

#### 章の参照

章・節・項は、それぞれ以下の記法を用いる。
```
== 章の名前
=== 節の名前
==== 項の名前
```

あるセクションを文書内で参照するには、まずセクション名の上にアンカー（`[[...]]`）を入れる。
```
[[toc:introduction]]
== 序論

ここに研究の序論を書く。
```

その後、文書内では以下のように``<<アンカー名,表示名>>``の記法でリンクを作成することで参照する。
```
<<toc:introduction,序論>> で述べた通り、・・・
```

#### 図表・コードのアンカー

図表・コードの参照方法もアンカーの付与→リンク作成の手順で行う。以下はコードの例。

```
[[code:sample]]
[source,ruby]  
----
require 'sinatra'

get '/hi' do
  "Hello World!"
end
----
```

#### 引用文献のアンカー

引用文献の書誌事項は`reference.adoc`にまとめて書く。
```
[bibliography]
== 引用文献
- [[[Hunt:99]]] Andy Hunt & Dave Thomas. The Pragmatic Programmer: From Journeyman to Master. Addison-Wesley. 1999.
- [[[Allen:08]]] Dan Allen. Seam in Action. Manning Publications.2008.
```


#### アンカータグの例

アンカーに使うタグは統一しておくとよい

- 章・節・項：`toc:○○`
- 図：`fig:○○`
- 表：`tbl:○○`
- コード：`code:○○`
- 引用：`第一著者名字:出版年`（例：`Joho:2020`）

## AsciiDoctorのレファレンス

- https://github.com/asciidoctor/asciidoctor/blob/master/README-jp.adoc
