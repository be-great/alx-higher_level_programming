#!/usr/bin/python3
"""
module That prints a square with the character #.
size is the size length of the square
size must be an integer, otherwise raise a TypeError
"""


def print_square(size):
    """
    args: (int)size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()
