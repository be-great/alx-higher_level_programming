#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # find the key
    list_of_key = [key for key, val in a_dictionary.items() if val == value]

    # delete value that key
    for key in list_of_key:
        del a_dictionary[key]
    new_dic = a_dictionary.copy()
    return new_dic
