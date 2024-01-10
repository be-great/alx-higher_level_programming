#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """
    Function that returns a list with all values multiplied by
    a number without using any loops.
    function_mul = lambda x: x * number
    """
    res_ = list(map(lambda x: x * number, my_list))
    return res_
