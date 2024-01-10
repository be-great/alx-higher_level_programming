#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """function that returns a new dictionary with all values multiplied by 2
    """
    new_dic = {key : value * 2 for key , value in a_dictionary.items()}
    return new_dic
