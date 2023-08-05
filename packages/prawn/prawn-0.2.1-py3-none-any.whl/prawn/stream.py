"""
Read in one stream that is a mix of potential html and text and convert any
html to text
"""

import re

import html2text


def process_stream(fin, fout):
    """
    Read a line at a time, look for HTML and if observed convert to text.
    """
    for line in fin:
        if looks_html(line):
            line = html2text.html2text(line)
        fout.write(line)
        fout.flush()


def looks_html(line):
    """
    Look for clues of html in the first 128 characters
    """
    start = line[:128]
    if "<pre>" in start:
        return True
    return re.search('&#x[0-9A-F]{1,6};', start) is not None
