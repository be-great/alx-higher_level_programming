#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    # it will return list of the keys
    sorted_dic = sorted(a_dictionary)

    for key in sorted_dic:
        print("{:}: {}".format(key, a_dictionary[key]))
    