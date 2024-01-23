#!/usr/bin/python3
"""this is a program that have a class with private attribute"""


class Square:
    """a class have:
    size : Private instance attribute
    with exception handling
    """
    def __init__(self, size=0):
        """a private instance attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance method that returns the current square area"""

        return self.__size ** 2

    @property
    def size(self):
        """get the size instance attribute"""

        return self.__size

    @size.setter
    def size(self, value):
        """set the size instance attribute"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Check if two squares are equal based on area."""

        if not isinstance(other, Square):
            return False
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal based on area."""

        if not isinstance(other, Square):
            return False
        return not self.__eq__(other)

    def __gt__(self, other):
        """Check if the area of the current square is
        greater than the other."""

        if not isinstance(other, Square):
            return False
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the area of the current square is
        greater than or equal to the other."""

        if not isinstance(other, Square):
            return False
        return self.area() >= other.area()

    def __lt__(self, other):
        """Check if the area of the current square is
        less than the other."""

        if not isinstance(other, Square):
            return False
        return self.area() < other.area()

    def __le__(self, other):
        """Check if the area of the current square is
        less than or equal to the other."""

        if not isinstance(other, Square):
            return False
        return self.area() <= other.area()
