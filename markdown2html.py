#!/usr/bin/python3
"""
A script that convert a Markdown file to HTML.

Usage:
    ./markdown2html.py [markdown_file] [output_file]

Arguments:
    markdown_file: the name of the Markdown file to be converted
    output_file: the name of the output HTML file
"""

import argparse
import pathlib
import re
import sys


def convert_markdown_to_html(markdown_file, output_file):
    """
    Converts markdown file to HTML file
    """
    with open(markdown_file, encoding='utf-8') as f:
        markd_content = f.readlines()

    html_content = []
    for line in markd_content:
        match = re.match(r'(#){1,6} (.*)', line)
        if match:
            h_level = len(match.group(1))
            h_content = match.group(2)
            html_content.append(f'<h{h_level}>{h_content}</h{h_level}>\n')
        else:
            html_content.append(line)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(html_content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert markdown to HTML')
    parser.add_argument('input_file', help='path to input markdown file')
    parser.add_argument('output_file', help='path to output HTML file')
    args = parser.parse_args()

    input_path = pathlib.Path(args.input_file)
    if not input_path.is_file():
        print(f'Missing {input_path}', file=sys.stderr)
        sys.exit(1)

    # Convert the markdown file to HTML
    convert_markdown_to_html(args.input_file, args.output_file)
