#!/usr/bin/python3
"""
 function that returns True if the object is
 exactly an instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """
    args: (instance) obj, (class) a_class
    """
    # type(obj) is a_class ensures that the object
    # is not just an instance of a subclass of
    return isinstance(obj, a_class) and type(obj) is a_class
