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

    root_path = os.path.abspath('.').split(os.path.sep)[0] + os.path.sep
    transformer = etree.XSLT(open_etree(Path(args.xslt_file)))
    resolved_paths = []

    for xml_path in args.xml_paths:
        p = Path(xml_path)

        if p.is_file():
            resolved_paths.append(p)
        elif p.is_absolute():
            resolved_paths.extend(Path(root_path).glob(xml_path[len(root_path):]))
        else:
            resolved_paths.extend(Path(args.workdir).glob(xml_path))

    for path in resolved_paths:
        sys.stdout.write(str(transformer(open_etree(path))))
