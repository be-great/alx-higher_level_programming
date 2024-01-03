#!/usr/bin/python3

""" Using slicing:-
    my_string = my_string[:n] + my_string[m+1:]
"""


def remove_char_at(str, n):
    # 1- check if position is right
    if n >= len(str):
        return str
    # 2- check if position is negative
    if n < 0:
        n = len(str) - n
    # slice it
    str = str[:n] + str[n+1:]
    return str
