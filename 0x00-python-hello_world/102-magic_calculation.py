#!/usr/bin/python3
import dis
"""
3           0 LOAD_CONST   1 (98) # load const to the stack
3           3 LOAD_FAST    0 (a)  # load variable name a to stack
3           6 LOAD_FAST    1 (b)  # load variable name b to stack
3           9 BINARY_POWER  # rise the b**a (last on the stack)
3          10 BINARY_ADD    # add result of previous b**a + 98
3          11 RETURN_VALUE  # return the last operation
"""


def magic_calculation(a, b):
    re = b**a
    return re + 98
