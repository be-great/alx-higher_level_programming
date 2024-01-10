#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """Write a function that deletes a key in a dictionary.
    """
    # check if key exist or not
    if key in a_dictionary:
        del a_dictionary[key]
