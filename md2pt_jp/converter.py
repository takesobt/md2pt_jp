# md2pt_jp/converter.py にこれがある前提
from typing import Optional
import re

def convert_markdown_to_plaintext(markdown_text: str) -> str:
    text = re.sub(r'^\s*#+\s*', '', markdown_text, flags=re.MULTILINE)
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    return text.strip()


# def convert_markdown_to_plaintext(markdown_text: str) -> str:
#     """
#     Markdown形式のテキストを、プレーンテキストに変換する。

#     主な変換ルール：
#     - 見出し（#）は削除して改行に
#     - 強調（**text**）は強調記号を削除
#     - 箇条書き（- や 1.）は削除 or ・に置換
#     - インラインコードは削除
#     - 空行は段落として残す
#     """

#     # ヘッダー削除：#や##などを消して改行扱いに
#     text = re.sub(r'^\s*#+\s*', '', markdown_text, flags=re.MULTILINE)

#     # 強調記号の削除（**text** → text）
#     text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)

#     # イタリック（*text*）の削除
#     text = re.sub(r'\*(.*?)\*', r'\1', text)

#     # 箇条書きの置換（- item → ・item）
#     text = re.sub(r'^\s*[-*+]\s+', '・', text, flags=re.MULTILINE)

#     # 番号付きリスト（1. item → ・item）
#     text = re.sub(r'^\s*\d+\.\s+', '・', text, flags=re.MULTILINE)

#     # インラインコード（`code`）の削除
#     text = re.sub(r'`(.*?)`', r'\1', text)

#     # HTMLの<br>を改行に
#     text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)

#     # 不要な複数連続空行を1つに
#     text = re.sub(r'\n{3,}', '\n\n', text)

#     return text.strip()
