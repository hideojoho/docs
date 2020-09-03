# Flutter

:bulb: Flutterはクロスプラットフォームなモバイルアプリを構築する開発環境です

## 準備

- [Git for Windows](pc-git.md)
- [VSCode](pc-vscode.md)
- [Chrome](pc-essential-apps.md)

## 作業用フォルダの作成

- [第2作業エリア](../../pc-workspace.md)に作業用フォルダ（`flutter`）を作成
```
PS C:\Users\アカウント名> mkdir C:\Home\sNNNNNNN\Workspace\flutter
```

## インストール

### Flutter

- [Flutterのダウンロード](https://flutter.dev/docs/get-started/install/windows)にいき、`flutter_windows_x.xx.x-stable.zip`をダウンロード
  - 以下の説明では自分がダウンロードしたバージョンに置き換えること
- ダウンロードしたZipファイルを解凍
- 解凍されたフォルダ（例：`flutter`）を[第2作業エリア](pc-workspace.md)（例 `C:\Home\sNNNNNNN`）に移動

### 環境変数の設定

- `Ctrl+S`で検索窓を開き、`env`と入力 → 「システム環境変数の編集」を選択
- 「システムプロパティ」ウィンドウが開くので、「詳細設定」タブの一番下にある「環境変数」を選択
- 「ユーザの環境変数」パネル変数一覧から`Path`を選択し、「編集」ボタンをクリック
- Path変数のリストが表示されたら、右パネルから「新規」を選択
- リストに`C:\Home\sNNNNNNN\flutter\bin`を入力し、OKをクリック
- `Windows PowerShell`を新規起動し、以下のコマンドを実行してメッセージが表示されたら成功

```
PS C:\Users\ユーザ名> flutter doctor
Doctor summary (to see all details, run flutter doctor -v):
[✓] Flutter (Channel stable, 1.20.3, on Microsoft Windows [Version 10.0.19041.450], locale ja-JP)
[✗] Android toolchain - develop for Android devices
    ✗ Unable to locate Android SDK.
      Install Android Studio from: https://developer.android.com/studio/index.html
      On first launch it will assist you in installing the Android SDK components.
      (or visit https://flutter.dev/docs/get-started/install/windows#android-setup for detailed instructions).
      If the Android SDK has been installed to a custom location, set ANDROID_SDK_ROOT to that location.
      You may also want to add it to your PATH environment variable.

[!] Android Studio (not installed)
[✓] VS Code (version 1.48.2)
[!] Connected device
    ! No devices available

! Doctor found issues in 3 categories.
```

### Web環境の設定

- `Windows PowerShell`を新規起動し、以下のコマンドを実行

```
PS C:\Users\ユーザ名> flutter channel beta
PS C:\Users\ユーザ名> flutter upgrade
PS C:\Users\ユーザ名> flutter config --enable-web
```

- デバイスの確認
  - 表示されるブラウザは異なる可能性があります

```
PS C:\Users\ユーザ名> flutter devices
3 connected devices:

Web Server (web) • web-server • web-javascript • Flutter Tools
Chrome (web)     • chrome     • web-javascript • Google Chrome 84.0.4147.135
Edge (web)       • edge       • web-javascript • Microsoft Edge 85.0.564.44
```

## VSCodeの設定とプロジェクトの作成

- VSCodeを起動し、`flutter`拡張機能をインストール
- `Ctrl+Shift+P`でコマンドパレットを表示し、`flutter`と入力 → 「Flutter: New Project」を選択
- `Enter a name for your new project`で`myapp`と入力
- フォルダの選択画面で、作業用フォルダ（例：`C:\Home\sNNNNNNN\Workspace\flutter`）を選択
  - プロジェクトが生成されるまで待つ

## プロジェクトの実行

- プロジェクトの生成が完了したら、上部メニュー → 実行 → デバッグの開始 を選択
- `Select a device to use`から`Enable Chrome`を選択
- セキュリティ警告が表示されたら「アクセスを許可する」を選択
- 自動的にChromeが起動しない場合は、http://localhost:59222/ にいく


## アプリ開発

- https://flutter.dev/docs/get-started/codelab


## URLs

- https://flutter.dev/docs/get-started/install/windows