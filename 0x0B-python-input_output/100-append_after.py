#!/usr/bin/python3
"""
function that inserts a line of
text to a file, after each line
containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    args: (str) filename, (str) search_string
          (str) new_string
    """

    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
