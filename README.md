# md2pt_jp
## Version 1.1

Markdownで書かれた日本語小説を、小説投稿サイト（例：「小説家になろう」など）向けのプレーンテキストに変換するツールです。

## ✅ 対応している変換

- 見出し：
  - `###見出し3` → `【見出し3】`
  - `##見出し2` → `★★見出し2★★`
  - `#見出し1` → `☆EPISODE☆見出し1`
- 強調（`**強調**`）→ 強調マークを削除
- 箇条書き → `・` に置換
- 区切り線 `---` → `＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝`
- その他細かいMarkdown記法の除去

## 🚀 使い方

### ① 単一ファイルを変換

```bash
poetry run python -m md2pt_jp.cli input.md output.txt
```

### ② フォルダ内の .md ファイルを一括変換
・input_folder/ 配下のすべての .md ファイルを .txt に変換します。
・サブフォルダの .md ファイルは無視されます。
```bash
poetry run python -m md2pt_jp.cli input_folder/ output_folder/
```
### ③ サブフォルダも含めて再帰的に一括変換
・--recursive オプションを指定すると、サブフォルダも含めて .md ファイルを探索します。
・出力先には同じフォルダ構造が再現されます。
```bash
poetry run python -m md2pt_jp.cli input_folder/ output_folder/ --recursive
```
### ④ 既存の .txt を上書きしたい場合
・デフォルトでは、出力先に同名の .txt があると処理は中断されます。
・--overwrite をつけると、既存ファイルを強制的に上書きします。
```bash
poetry run python -m md2pt_jp.cli input_folder/ output_folder/ --recursive --overwrite
```