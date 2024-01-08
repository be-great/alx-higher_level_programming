#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    new_list = [x for x in my_list]
    return new_list
