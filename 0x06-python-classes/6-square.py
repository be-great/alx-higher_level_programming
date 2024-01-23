#!/usr/bin/python3
"""this is a program that have a class with private attribute"""


class Square:
    """a class have:
    size : Private instance attribute
    with exception handling
    """

    def __init__(self, size=0, position=(0, 0)):
        """a private instance attribute"""

        self.size = size
        self.position = position

    def area(self):
        """Public instance method that returns the current square area"
         Arguments:
            size (int): The size of the new square.
            position (int, int): The position of the new square."""

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

    @property
    def position(self):
        """get the position instance attribute"""

        return self.__position

    @position.setter
    def position(self, value):
        """set the position instance attribute"""

        is_int = all(isinstance(x, int) and x >= 0 for x in value)
        is_tuple = isinstance(value, tuple)
        if len(value) != 2 or not is_int or not is_tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #"""

        size = self.__size
        pos = self.__position
        if self.__size <= 0:
            print()
        else:
            for i in range(0, pos[1]):
                print()

            for j in range(0, size):
                print(" " * pos[0], end="")
                print("#" * size)
