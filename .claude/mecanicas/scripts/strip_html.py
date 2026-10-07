#!/usr/bin/env python3
"""Quita tags de un HTML y deja el texto visible, uno por línea.

Uso: curl -sL <url> | python3 strip_html.py
"""
import os
import re
import sys
from html.parser import HTMLParser

CHARSET_RE = re.compile(rb'charset=["\']?([\w-]+)', re.IGNORECASE)

SKIP_TAGS = {"script", "style", "noscript", "template"}
BLOCK_TAGS = {
    "p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6",
    "section", "article", "header", "footer", "nav",
}


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.chunks = []
        self.skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in SKIP_TAGS:
            self.skip_depth += 1
        elif tag in BLOCK_TAGS:
            self.chunks.append("\n")

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS and self.skip_depth:
            self.skip_depth -= 1
        elif tag in BLOCK_TAGS:
            self.chunks.append("\n")

    def handle_data(self, data):
        if not self.skip_depth:
            self.chunks.append(data)


def main():
    raw = sys.stdin.buffer.read()
    match = CHARSET_RE.search(raw[:2048])
    charset = match.group(1).decode("ascii") if match else "utf-8"
    try:
        html = raw.decode(charset, errors="replace")
    except LookupError:
        html = raw.decode("utf-8", errors="replace")

    parser = TextExtractor()
    parser.feed(html)
    text = "".join(parser.chunks)
    lines = [line.strip() for line in text.splitlines()]
    try:
        for line in lines:
            if line:
                print(line)
    except BrokenPipeError:
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        sys.exit(0)


if __name__ == "__main__":
    main()
