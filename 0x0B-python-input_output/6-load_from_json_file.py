#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """
    args: (str) filename
    """
    with open(filename, 'r') as file:
        return json.load(file)
