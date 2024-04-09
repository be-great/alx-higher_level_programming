#!/usr/bin/python3
"""
class Student that defines a student by

Public method def reload_from_json(self, json)
that replaces all attributes of the Student instance:

-You can assume json will always be a dictionary
-A dictionary key will be the public attribute name
-A dictionary value will be the value of the public attribute

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

    def reload_from_json(self, json_data):
        """replaces all attributes of the Student instance"""
        for key, value in json_data.items():
            setattr(self, key, value)
