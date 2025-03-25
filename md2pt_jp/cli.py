import argparse
from pathlib import Path
import sys
from md2pt_jp.converter import convert_markdown_to_plaintext


def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert Markdown (.md) files to plain text (.txt) for novel posting sites."
    )
    parser.add_argument("input_path", type=Path, help="Path to input file or directory")
    parser.add_argument("output_dir", type=Path, help="Path to output directory")
    parser.add_argument("--recursive", action="store_true", help="Recursively search subdirectories for .md files")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing output files")
    return parser.parse_args()


def collect_md_files(input_path: Path, recursive: bool) -> list[Path]:
    if input_path.is_file() and input_path.suffix == ".md":
        return [input_path]
    elif input_path.is_dir():
        pattern = "**/*.md" if recursive else "*.md"
        return list(input_path.glob(pattern))
    else:
        sys.exit(f"Error: {input_path} is not a valid .md file or directory.")


def compute_output_path(input_file: Path, input_base: Path, output_base: Path) -> Path:
    relative_path = input_file.relative_to(input_base).with_suffix(".txt")
    return output_base / relative_path


def main():
    args = parse_args()

    md_files = collect_md_files(args.input_path, args.recursive)

    if not md_files:
        sys.exit("No .md files found to convert.")

    for md_file in md_files:
        output_path = compute_output_path(md_file, args.input_path, args.output_dir)

        if not args.overwrite and output_path.exists():
            sys.exit(f"Error: Output file already exists: {output_path}")

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with md_file.open("r", encoding="utf-8") as f:
            md_content = f.read()

        plain_text = convert_markdown_to_plaintext(md_content)

        with output_path.open("w", encoding="utf-8") as f:
            f.write(plain_text)

        print(f"Converted: {md_file} → {output_path}")

    print("✅ All files converted successfully.")


if __name__ == "__main__":
    main()
