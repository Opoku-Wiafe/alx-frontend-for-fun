#!/usr/bin/python3
"""
A script that converts a Markdown file to HTML.

Usage:
    ./markdown2html.py [markdown_file] [output_file]

Arguments:
    markdown_file: Name of the file to be converted.
    output_file: Name of the converted HTML file.
"""

import sys
import os
import markdown

def main():
    """
    A script markdown2html.py that takes two arguments: a markdown file name
    and an HTML file name for output.
    """
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_fname = sys.argv[1]
    html_fname = sys.argv[2]

    if not os.path.exists(markdown_fname):
        print(f"Missing {markdown_fname}", file=sys.stderr)
        sys.exit(1)

    with open(markdown_fname, 'r') as md_file:
        md_content = md_file.read()

    html_content = markdown.markdown(md_content)

    with open(html_fname, 'w') as html_file:
        html_file.write(html_content)

    sys.exit(0)

if __name__ == "__main__":
    main()
