# Windows Subsystem for Linux 1 (WSL-1)

:warning: この手順書は古いので、[WSL-2](pc-wsl-2.md)を参考にしてください。

:bulb: WSLとは、Windows 10に`Ubuntu`などのLinuxのディストリビューションをインストールするための仕組みです。

## 所要時間

- 15分

## 手順

### インストール

- 管理者として `Windows PowerShell` を起動し、以下のコマンドを実行

```
PS C:\Users\アカウント名> dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

- PCを再起動する
- ログイン後、`Ctrl+S`で`Store`と入力しMicrosoft Storeを起動
- Microsoft Storeの検索ボックスで「Ubuntu 18.04」と入力（:warning: Ubuntu 20.04とWSL-1は相性が良くない場合があるので18.04をお勧めします）
- 指示に従ってインストール
- Ubuntu 18.04の画面が起動したら、パスワードなどを設定する

### Linuxの起動

`Windows PowerShell`から以下のコマンドを実行

```
PS C:\Users\アカウント名> wsl
アカウント名@DESKTOP-○○○○:/mnt/c/Users/アカウント名$
```

### Linuxの再起動

- インストールされているディストリビューションの名前を調べる

```
PS C:\Users\アカウント名> wsl -l
Windows Subsystem for Linux ディストリビューション:
Ubuntu-18.04 (既定)
```

- 以下のコマンドを実行して再起動

```
PS C:\Users\アカウント名> wsl -t Ubuntu-18.04
```

## 参考URL

- [Windows 10 用 Windows Subsystem for Linux のインストール ガイド](https://docs.microsoft.com/ja-jp/windows/wsl/install-win10)
