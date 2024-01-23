#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        x = sys.exc_info()[1]
        print("Exception: {}".format(x), file=sys.stderr)
        return (False)
