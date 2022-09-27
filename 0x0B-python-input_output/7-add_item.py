#!/usr/bin/python3
import sys
"""Module 7-add_item.
A script that adds all arguments to a Python list,
and then saves them to a file.
"""


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


def add_item(args, filename):
    """adds args to a python list and saves them to a json file
    Args:
        -args: arguments
        -filename: name of json file
    """
    try:
        f = load(filename)
    except:
        f = []
    for s in args:
        f.append(s)
    save(f, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    filename = "add_item.json"
    add_item(args, filename)


