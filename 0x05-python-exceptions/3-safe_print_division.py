#!/usr/bin/python3

def safe_print_division(a, b):
    """a function that divides 2 integers and prints the result.
    Prototype"""
    result = 0
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
