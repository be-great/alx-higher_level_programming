#!/usr/bin/python3

"""
class Square that inherits from Rectangle (9-rectangle.py):
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    args: (superclass) Base => Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """args: same as teh Rectangle (superclass)"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return : [Square] (<id>) <x>/<y> - <size> """
        string = "[Square] ("
        string += str(self.id) + ") "
        string += str(self.x) + "/"
        string += str(self.y) + " - "
        string += str(self.width)
        return string

    @property
    def size(self):
        """get the size instance attribute"""

        return self.width

    @size.setter
    def size(self, value):
        """set the size instance attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle with the provided arguments.
        Args:
            (list) *args
        """
        attr = ["id", "size", "x", "y"]
        i = 0
        while i < len(args) and i < len(attr):
            if i == 1:
                setattr(self, "width", args[i])
                setattr(self, "height", args[i])
            else:
                setattr(self, attr[i], args[i])
            i += 1
        for key, value in kwargs.items():
            if key == "size":
                setattr(self, "width", value)
                setattr(self, "height", value)
            else:
                setattr(self, key, value)

    def to_dictionary(self):
        """
        returns the dictionary representation of a Square
        """
        dictionary = {
                "id": self.id,
                "x": self.x,
                "size": self.width,
                "y": self.y
        }
        return dictionary
