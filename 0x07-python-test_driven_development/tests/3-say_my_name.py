#!/usr/bin/python3
"""
function that prints My name is <first name> <last name>
first_name and last_name must be strings otherwise,
raise a TypeError exception with the message
"""


def say_my_name(first_name, last_name=""):
    """
    function that prints My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if len(first_name) != 0 or len(last_name) != 0:
        print("My name is {} {}".format(first_name, last_name))
