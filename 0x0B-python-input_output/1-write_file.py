#!/usr/bin/python3

"""
 function that writes a string to a text file (UTF8)
 and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    args: (str) filename, (str) text
    """

    with open(filename, 'w', encoding='utf-8') as file:
        len = file.write(text)
        return (len)
