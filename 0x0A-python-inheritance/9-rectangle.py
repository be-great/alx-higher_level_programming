#!/usr/bin/python3

"""
class Rectangle
that inherits from BaseGeometry (7-base_geometry.py).
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherite from teh BaseGemoetry
    """
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """implementing the area method"""
        return self.__width * self.__height

    def __str__(self):
        "return : [Rectangle] <width>/<height> "
        string = "[Rectangle] " + str(self.__width)
        string += "/" + str(self.__height)
        return string
