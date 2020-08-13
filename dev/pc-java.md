# Java

Javaアプリの実行ならばJava SDKを、Javaで書かれたアプリ開発をする場合はAntやMavenもインストールしましょう。

## 環境

- Java 14.0.2
- Ant 1.10.8
- Maven

## 所要時間

- 30分

## インストール

### Java


### Ant


### Maven

- TODO

## 環境変数の設定

- `Ctrl+S`で検索窓を開き、`env`と入力 → 「システム環境変数の編集」を選択
- 「システムプロパティ」ウィンドウが開くので、「詳細設定」タブの一番下にある「環境変数」を選択

### Java

- 「ユーザの環境変数」パネルの下から「新規」を選択
- 以下を入力し、OK
  - 変数名：`JAVA_HOME`
  - 変数値：`C:\Home\sNNNNNNN\jdk-14.0.2`
- 次に変数一覧から`Path`を選択し、「編集」ボタンをクリック
- Path変数のリストが表示されたら、右パネルから「新規」を選択
- リストに`%JAVA_HOME%\bin`を入力し、OKをクリック
- `Windows PowerShell`を新規起動し、以下のコマンドを実行してバージョン情報が表示されたら成功

```
PS C:\Users\ユーザ名> java -version
openjdk version "14.0.2" 2020-07-14
OpenJDK Runtime Environment (build 14.0.2+12-46)
OpenJDK 64-Bit Server VM (build 14.0.2+12-46, mixed mode, sharing)
```

### Ant

- 「ユーザの環境変数」パネルの下から「新規」を選択
- 以下を入力し、OK
  - 変数名：`ANT_HOME`
  - 変数値：`C:\Home\sNNNNNNN\apache-ant-1.10.8`
- 次に変数一覧から`Path`を選択し、「編集」ボタンをクリック
- Path変数のリストが表示されたら、右パネルから「新規」を選択
- リストに`%ANT_HOME%\bin`を入力し、OKをクリック
- `Windows PowerShell`を新規起動し、以下のコマンドを実行してバージョン情報が表示されたら成功

```
PS C:\Users\ユーザ名> and -version
Apache Ant(TM) version 1.10.8 compiled on May 10 2020
```

### Maven

- TODO
