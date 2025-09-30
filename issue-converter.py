#!/usr/bin/env python3

import os
import sys

from lxml import etree
from pathlib import Path

def open_etree(f):
    with open(f) as fd:
        parser = etree.XMLParser()
        return etree.parse(fd, parser)

def resolve_paths(inputs):
    root_path = os.path.abspath(os.getcwd()).split(os.path.sep)[0] + os.path.sep
    resolved_paths = []

    for path in inputs:
        p = Path(path.strip())

        if p.is_file():
            resolved_paths.append(p)
        elif p.is_absolute():
            resolved_paths.extend(Path(root_path).glob(path[len(root_path):]))
        else:
            resolved_paths.extend(Path(os.getcwd()).glob(path))
    
    return resolved_paths

def gtest_to_generic_execution(resolved_inputs, output):
    test_executions = etree.Element("testExecutions")
    test_executions.set("version", "1")

    transformer = etree.XSLT(open_etree(Path(os.getenv("GITHUB_ACTION_PATH")) / "converters" / "gtest-to-generic-execution.xslt"))
    parser = etree.XMLParser(remove_blank_text=True)

    for path in resolved_inputs:
        transformed_tree = str(transformer(open_etree(path)))
        for execution in etree.fromstring(f"<root>{transformed_tree}</root>", parser):
            test_executions.append(execution)

    document = etree.ElementTree(test_executions)
    document.write(output, pretty_print=True, xml_declaration=False, encoding='UTF-8')

if __name__ == "__main__":
    try:
        transformation = os.getenv("TRANSFORMATION", "")
        inputs = os.getenv("INPUT")
        output = os.getenv("OUTPUT")

        resolved_inputs = resolve_paths(inputs.splitlines())

        if transformation == "gtest-to-generic-execution":
            gtest_to_generic_execution(resolved_inputs, Path(output))
        else:
            raise Exception(f"Unknown transformation {transformation}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
