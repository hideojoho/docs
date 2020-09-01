# PC内作業エリアの作成

## 本作業の背景

### その１

- 研究室PCは`Synology Drive`というアプリを用いて、研究室内サーバと双方向同期をするように設定します。
- そのために、個人用ファイルを保存する`MyFolders`と研究室全体で共有する`TeamFolders`（読み取り専用）の二つを作成しておきます。

### その２

- 研究室PCは[Office365のアカウント](https://github.com/joholabhq/docs/blob/ja/onboarding/getting-started.md)でログインすることを想定しています。
- これによりアカウント名が自動的に日本語になる場合があります。これはホームフォルダのパスに日本語が含まれることを意味します。
  - 現状では、Office365のアカウント名は変更できないようです
- インストールするプログラムによっては、ホームフォルダのパスに日本語が含まれていると正常に動作しないことがあります。
- したがって、日本語を含まない場所にもう一つのホームフォルダ（第２作業エリア）を作成し、必要に応じて使い分けます。

## 所要時間

- 5分

## 手順1：デフォルトの作業エリア（第１作業エリア）

- `Windows PowerShell`を起動し、以下のコマンドを実行（エクスプローラーで作業しても良い）
```
PS C:\Users\アカウント名>mkdir SynologyDrive; cd SynologyDrive
PS C:\Users\アカウント名\SynologyDrive>mkdir MyFolders; mkdir TeamFolders; cd TeamFolders
PS C:\Users\アカウント名\SynologyDrive\TeamFolders>mkdir Lab
```
- 結果
```
C:
  ├ Users
    ├ アカウント名
      ├ SynologyDrive
        ├ TeamFolders
          ├ Lab # ここに研究室全体の共有フォルダを同期設定する
        ├ MyFolders
          ├ # ここに個人の研究関連ファイルやデータを置く
          
```
- [Synology Drive](pc-synologydrive.md)をインストール

## 手順2: 第２作業エリア

- `Windows PowerShell`を起動し、以下のコマンドを実行（エクスプローラーで作業しても良い）
- `sNNNNNNN`は統一認証のユーザ名（半角英数）
```
PS C:\Users\アカウント名>cd C:\
PS C:\>mkdir Home; cd Home
PS C:\Home>mkdir sNNNNNNN; cd sNNNNNNN
PS C:\Home\sNNNNNNN>mkdir Workspace; cd Workspace
```
- 結果
```
C:
  ├ Home
    ├ sNNNNNNN
      ├ Workspace
        ├ ここにフォルダやファイルを保存する
```
