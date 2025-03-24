import sys
from md2pt_jp.converter import convert_markdown_to_plaintext

def main():
    if len(sys.argv) != 3:
        print("使い方: python cli.py 入力ファイル.md 出力ファイル.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            markdown_text = f.read()
    except FileNotFoundError:
        print(f"入力ファイルが見つかりません: {input_file}")
        sys.exit(1)

    converted_text = convert_markdown_to_plaintext(markdown_text)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(converted_text)

    print(f"変換完了！ → {output_file}")

if __name__ == "__main__":
    main()
