#!/usr/bin/python3

"""
function function that returns an object
representation of an object (string)
"""
import json


def from_json_string(my_str):
    """
    args : (str) my_str
    """
    return json.loads(my_str)
