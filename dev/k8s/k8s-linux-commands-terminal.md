# Jupyter Lab ターミナル Linxuコマンド集

:bulb: 以下の説明はJupyter Labのターミナルを使って実行する方法です。
Jupyter Notebook内のセルから実行するコマンド類の説明は[こちら](k8s-linux-commands.md)です。

## 前提

- [研究室クラスターの使い方](README.md)

## Linxuコマンドの実行方法

### tmux

:bulb: `tmux`は実行中のターミナルを「閉じたり・再開したり」することができるツール。完了に長時間要するプロセスを走らせるときに便利です。

- tmuxがインストールされているイメージ（2020/09現在）
  - `hideojoho/jupyter-jdk`

- tmuxの起動

```
$ tmux
```

- tmux画面を閉じずに出る方法

```
$ ctrl+B → d
```

- 起動中のtmux画面一覧

```
$ tmux ls
```

- 起動中のtmux画面に再接続する方法

```
$ tmux attach -t 0 # or 1 or ...
```

- 起動中のtmux画面を終了する方法

```
exit
```

- スクロールモードを有効にする

:warning: `tmux`は通常モードではスクロールできません。

```
Ctrl+B → [
```

- スクロールモードを無効にする

```
ESC
```
- URLs
  - https://github.com/tmux/tmux/wiki
