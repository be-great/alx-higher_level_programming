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

    def my_print(self):
        """prints in stdout the square with the character #"""

        size = self.__size
        if self.__size <= 0:
            print()
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
