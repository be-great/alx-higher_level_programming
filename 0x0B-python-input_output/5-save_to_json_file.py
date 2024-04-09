#!/usr/bin/python3
"""
 function that writes an Object to
 a text file, using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """
    args:(str) my_obj, (str)v filename
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
