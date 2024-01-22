#!/usr/bin/python3

def safe_print_integer(value):
    """function that prints an integer with "{:d}".format()."""
    try:
        print("{:d}\n".format(value))
        return (True)
    except ValueError:
        return (False)
