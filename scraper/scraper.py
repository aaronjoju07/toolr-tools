import os
import argparse
import sys

DEFAULT_OUTPUT_DIR = os.path.expanduser("~/Documents/")

def print_help():
    help_text = """
Scraper CLI Tool - Code Aggregator

Usage:
  python scraper.py <source_directory> <output_filename> [-o <output_path>] [-f]

Arguments:
  <source_directory>      Required. Path to the directory you want to scrape.
  <output_filename>       Required. Name of the output file (e.g., backend.txt)
  -o, --output <path>     Optional. Output folder. Default is: ~/Documents/
  -h, --flags             Show this help message.

Example:
  python scraper.py ./myproject final.txt
  python scraper.py ./myproject backend.txt -o ~/Desktop/
"""
    print(help_text)

def copy_files_to_main_file(source_dir, output_file_path, exclusions):
    with open(output_file_path, 'w', encoding='utf-8') as main_file:
        for root, dirs, files in os.walk(source_dir):
            dirs[:] = [d for d in dirs if d not in exclusions['dirs']]
            for file in files:
                if file in exclusions['files']:
                    continue
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, start=source_dir)
                try:
                    main_file.write(f"\n// relative path: {relative_path}\n")
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        main_file.write(f.read())
                        main_file.write("\n")
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    print(f"✅ Scraped content saved to: {output_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("source", nargs="?", help="Source directory to scrape")
    parser.add_argument("filename", nargs="?", help="Output file name (e.g., backend.txt)")
    parser.add_argument("-o", "--output", help="Output folder", default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("-h", "--flags", action="store_true", help="Show CLI help")

    args = parser.parse_args()

    if args.flags or not args.source or not args.filename:
        print_help()
        sys.exit(0)

    exclusions = {
        'dirs': ['bin', 'obj', 'Properties', 'node_modules', '.git'],
        'files': ['package-lock.json', '.gitignore', 'favicon.ico', '.env', '.DS_Store']
    }

    if not os.path.exists(args.source):
        print(f"❌ Source directory not found: {args.source}")
        sys.exit(1)

    os.makedirs(args.output, exist_ok=True)
    output_file_path = os.path.join(args.output, args.filename)

    copy_files_to_main_file(args.source, output_file_path, exclusions)
