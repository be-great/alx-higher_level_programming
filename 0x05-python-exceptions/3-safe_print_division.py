#!/usr/bin/python3

def safe_print_division(a, b):
    """a function that divides 2 integers and prints the result.
    Prototype"""
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))
    return result
