#!/usr/bin/python3
"""
class will be the “base” of
all other classes in this project
"""


class Base:
    """
    this a the base class
    to manage the id attribute
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """args: (int) id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

