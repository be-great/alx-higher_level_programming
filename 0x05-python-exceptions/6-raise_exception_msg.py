#!/usr/bin/python3

def raise_exception_msg(message=""):
    """function that raises a name exception with a message."""
    try:
        # use undefined variable
        print(x)
    except NameError as e:
        raise NameError(message) from e
