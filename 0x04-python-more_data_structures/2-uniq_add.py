#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ function that add uniq element only
        Using set: (only have uniq element)"""
    _set = set()

    # add to the set
    for num in my_list:
        _set.add(num)
    res = sum(_set)
    return res
