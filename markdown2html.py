#!/usr/bin/python3
"""
This script converts a Markdown file to HTML.

Usage:
    ./markdown2html.py [input_file] [output_file]

Arguments:
    input_file: The name of the Markdown file to be converted.
    output_file: The name of the output HTML file.
"""

import sys
import os
import markdown

def convert_markdown_to_html(markd_file, output_file):
    """
    Converts a markdown file to an HTML file.

    Args:
        markd_file: The markdown file to convert.
        output_file: The destination HTML file.
    """
    pass  # Placeholder for the function's implementation

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    input_file, output_file = sys.argv[1], sys.argv[2]

    if not os.path.isfile(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    convert_markdown_to_html(input_file, output_file)
