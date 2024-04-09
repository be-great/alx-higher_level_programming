#!/usr/bin/python3
"""
class Student that defines a student by
Public method def to_json(self, attrs=None):
that retrieves a dictionary representation of
a Student instance (same as 8-class_to_json.py):

-If attrs is a list of strings, only attribute names
        contained in this list must be retrieved.
-Otherwise, all attributes must be retrieved

"""


class Student:
    """
    args : first_name, last_name and age
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        If attrs is a list of strings, only attribute
        names contained in this list must be retrieved
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
