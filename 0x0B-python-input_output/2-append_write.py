#!/usr/bin/python3

"""
function that appends a string at the end
of a text file (UTF8)
and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """
    args: (str) filename , (str) text
    """
    with open(filename, 'a', encoding='utf-8') as file:
        len = file.write(text)
        return (len)
