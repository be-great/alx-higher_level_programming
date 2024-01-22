#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    length = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            length += 1
        except (ValueError, IndexError):
            continue
    print()
    return (length)
