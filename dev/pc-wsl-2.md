# Windows Subsystem for Linux 2 (WSL-2)

- :warning: この手順書は、`Windows 10 May 2020 Update`をインストールします。指導教員から指示があった場合のみ実行しましょう。
- :bulb: WSLとは、Windows 10に`Ubuntu`などのLinuxのディストリビューションをインストールするための仕組みです。

## 所要時間

- 2時間

## 手順

### Windows 10 May 2020 Updateのインストール

#### Windows Updateからインストール可能な場合

:bulb: 2020年8月17日現在、当該アップデートは利用可能になっていません。

- Windows Updateの指示に従ってください。

#### Microsoftのサイトからインストールする場合

- [Windows 10 のダウンロード - Microsoft](https://www.microsoft.com/ja-jp/software-download/windows10)にいく
- 「Windows 10 May 2020 Update」の「今すぐアップデート」を選択
- インストーラーをダウンロードし、実行
- インストーラーの指示にしたがってアップデート
- インストール完了後、再度Windows Updateを実行し、必要に応じて再起動

### WSL2のインストール

- 管理者として `Windows PowerShell` を起動し、以下のコマンドを実行

```
PS C:\Users\アカウント名> dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

- PCを再起動する
- 管理者として `Windows PowerShell` を起動し、以下のコマンドを実行

```
PS C:\Users\アカウント名> dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

- PCを再起動する
- [WSL 2 Linux カーネルの更新](https://docs.microsoft.com/ja-jp/windows/wsl/wsl2-kernel)の指示にしたがって、カーネルをインストール
- 以下のコマンドを実行し、WSL2を規定バージョンに設定

```
PS C:\Users\アカウント名> wsl --set-default-version 2
```

### Ubuntu 20.04のインストール

- `Ctrl+S`で`Store`と入力しMicrosoft Storeを起動
- Microsoft Storeの検索ボックスで「Ubuntu 20.04」と入力
- 指示に従ってインストール
- Ubuntu 20.04の画面が起動したら、パスワードなどを設定する

### Linuxの起動と停止

#### 起動

- `Windows PowerShell`から以下のコマンドを実行

```
PS C:\Users\アカウント名> wsl
アカウント名@DESKTOP-○○○○:/mnt/c/Users/アカウント名$
```

#### シャットダウン

- `Windows PowerShell`から以下のコマンドを実行

```
PS C:\Users\アカウント名> wsl --shutdown
```

## 参考URL

- [Windows 10 用 Windows Subsystem for Linux のインストール ガイド](https://docs.microsoft.com/ja-jp/windows/wsl/install-win10)
