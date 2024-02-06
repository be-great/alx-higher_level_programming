#!/usr/bin/python3
"""
 function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    args: (str) filename
    """
    with open(filename, 'r') as file:
        print(file.read(), end="")
