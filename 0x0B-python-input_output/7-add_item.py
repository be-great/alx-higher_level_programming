#!/usr/bin/python3
"""
script that adds all arguments to a
Python list, and then save them to a file:
"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    step1 = __import__('6-load_from_json_file')
    load_from_json_file = step1.load_from_json_file
    filename = "add_item.json"

    try:
        _list = load_from_json_file(filename)
    except FileNotFoundError:
        _list = []
    _list.extend(sys.argv[1:])
    save_to_json_file(_list, filename)
