#!/usr/bin/python3

"""
Write an empty class BaseGeometry.
"""


class BaseGeometry:
    """
    args: (instance) obj , (class) a_class
    """
    def area(self):
        """ show that we didn't implement the area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function that validate the value variable
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
