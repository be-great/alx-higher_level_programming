#!/usr/bin/python3
"""this is a program that have a class with private attribute"""
from models.base import Base


class Rectangle(Base):
    """
    a class have:
    size : Private instance attribute
    with exception handling
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        args: (int) width
              (int) height
              (int) x
              (int) y
              (int) id
        """

        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__height = height
        self.__width = width
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """get the width instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the size instance attribute"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the width instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the size instance attribute"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x instance attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the x instance attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y instance attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y instance attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """function to calculate the area"""

        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        result = "\n"*self.__y
        for h in range(self.__height):
            result += " " * self.__x + "#" * self.__width + "\n"
        print(result, end="")

    def __str__(self):
        """Returns:[Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id,
                        self.__x,
                        self.__y,
                        self.__width,
                        self.__height))

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle with the provided arguments.
        Args:
            (list) *args
        """
        attr = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            setattr(self, attr[i], args[i])

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle
        """
        dictionary = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
        }
        return dictionary
