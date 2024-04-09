#!/usr/bin/python3
"""
function that adds a new attribute to an object if it’s possible
"""


def add_attribute(class_name, attribute, value):
    """
    args: (class)     class_name
          (var)       attribute
          (any_type)  value
    """
    # check if the class or object have __dict__
    # if it have it that mean we can add attribute
    if not hasattr(class_name, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(class_name, attribute, value)
