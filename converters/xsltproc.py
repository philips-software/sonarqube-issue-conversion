#!/usr/bin/env python3

import argparse
import os
import sys

from lxml import etree
from pathlib import Path

def open_etree(f):
    with open(f) as fd:
        parser = etree.XMLParser()
        return etree.parse(fd, parser)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process XML files using XSLT transformations.")
    parser.add_argument("xslt_file", help="Path to the XSLT file.")
    parser.add_argument("xml_paths", nargs="+", help="Paths or glob patterns to the XML files to be transformed.")
    parser.add_argument("--workdir", default=".", help="Working directory to resolve relative paths.")
    args = parser.parse_args()

    transformer = etree.XSLT(open_etree(Path(args.xslt_file)))
    for xml_path in args.xml_paths:
        for path in Path(args.workdir).glob(xml_path):
            sys.stdout.write(str(transformer(open_etree(path))))
