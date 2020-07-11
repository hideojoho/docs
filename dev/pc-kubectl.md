# Kubectl

`kubectl`はKubernetesクラスター（通称`k8s`）の管理用スクリプトです。

## 所要時間

- 10分

## インストール手順

- [PowerShell Gallery](pc-advanced-apps.md#%E6%89%8B%E9%A0%86powershell-gallery%E3%82%92%E4%BD%BF%E3%81%86%E5%A0%B4%E5%90%88)が使えることを確認
- `PowerShell`を管理者権限で起動し、以下のコマンドを実行

```
C:\Users\アカウント名> Find-Package -Name install-kubectl                                                           
Name                           Version          Source           Summary
----                           -------          ------           -------
install-kubectl                1.7              PSGallery        This script is used during unsattended installs or to…

C:\Users\アカウント名> install-kubectl.ps1 'C:\Program Files\WindowsPowerShell\Modules\Kubectl'
==>Getting download link from  https://kubernetes.io/docs/tasks/tools/install-kubectl/
==>analyzing Downloadlink
==>starting Download from https://storage.googleapis.com/kubernetes-release/release/v1.18.0/bin/windows/amd64/kubectl.exe using Bitstransfer
==>starting 'C:\Program Files\WindowsPowerShell\Modules\Kubectl\kubectl.exe version'
error: Missing or incomplete configuration info.  Please point to an existing, complete config file:

  1. Via the command-line flag --kubeconfig
  2. Via the KUBECONFIG environment variable
  3. In your home directory as ~/.kube/config

To view or setup config directly use the 'config' command.

You can now start kubectl from C:\Program Files\WindowsPowerShell\Modules\Kubectl\kubectl.exe
copy your remote kubernetes cluster information to C:\Users\アカウント名\.kube/config
```

- `PowerShell`をユーザ権限で起動し、以下のコマンドを実行

```
C:\Users\アカウント名> kubectl version --client
Client Version: version.Info{Major:"1", Minor:"16+", GitVersion:"v1.16.6-beta.0", GitCommit:"e7f962ba86f4ce7033828210ca3556393c377bcc", GitTreeState:"clean", BuildDate:"2020-01-15T08:26:26Z", GoVersion:"go1.13.5", Compiler:"gc", Platform:"windows/amd64"}
```

## コンフィグファイルの設定

- コンフィグファイル（例：`admin.conf`）を指導教員から入手する
- 環境変数`KUBECONFIG`を設定する
  - `Win+S`→`env`と入力→「システム環境変数の変数」を選択
  - 「環境変数」を選択
  - 「ユーザ環境変数」→新規作成を選択
    - 変数名：`KUBECONFIG`
    - 変数値：コンフィグファイルの保存場所（C:\Users\アカウント名\SynologyDrive\MyFolders\Local\k8s\admin.conf`）
    - OK
  - OK→OK
- `PowerShell`を起動し、以下のコマンドを実行

```
C:\Users\アカウント名> echo $env:KUBECONFIG
C:\Users\アカウント名\SynologyDrive\MyFolders\Local\k8s\admin.conf
```
