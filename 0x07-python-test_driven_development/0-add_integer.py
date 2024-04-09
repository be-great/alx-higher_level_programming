#!/usr/bin/python3
"""
add_integer - Function that adds 2 integers.
a and b must be integers or floats, otherwise raise a TypeError
Return : a+b
"""


def add_integer(a, b=98):
    """
    args: (int)a, (int)b
    """

    # check if the a,b is instence of int and float only
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")

    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
