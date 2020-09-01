# Windows Subsystem for Linux 2 (WSL-2)

- :bulb: WSLとは、Windows 10に`Ubuntu`などのLinuxのディストリビューションをインストールするための仕組みです。

## 所要時間

- 2時間

## 手順

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
WSL 2 との主な違いについては、https://aka.ms/wsl2 を参照してください
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
