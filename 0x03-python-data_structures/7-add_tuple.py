#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    tuple_merge = ()
    for i in range(2):
        if i > len1 - 1 and i > len2 - 1:
            tuple_merge[i] = 0
        elif i > len1 - 1:
            tuple_merge += (tuple_b[i],)
        elif i > len2 - 1:
            tuple_merge += (tuple_a[i],)
        else:
            tuple_merge += (tuple_a[i] + tuple_b[i],)
    return tuple_merge
