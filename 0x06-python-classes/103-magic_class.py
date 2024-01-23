#!/usr/bin/python3
import math


class MagicClass:
    """Python class MagicClass
     0 LOAD_CONST               1 (0)
     3 LOAD_FAST                0 (self)
     6 STORE_ATTR               0 (_MagicClass__radius)
    load to the self.__MagicClass__radius a (0)
    """

    def __init__(self, redius=0):

        if type(redius) is not int and type(redius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = redius

    def area(self):
        """
         0 LOAD_FAST                0 (self)
              3 LOAD_ATTR                0 (_MagicClass__radius)
              6 LOAD_CONST               1 (2)
              9 BINARY_POWER
             10 LOAD_GLOBAL              1 (math)
             13 LOAD_ATTR                2 (pi)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """
        0 LOAD_CONST               1 (2)
              3 LOAD_GLOBAL              0 (math)
              6 LOAD_ATTR                1 (pi)
              9 BINARY_MULTIPLY
             10 LOAD_FAST                0 (self)
             13 LOAD_ATTR                2 (_MagicClass__radius)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE
        """
        return 2 * math.pi * self.__radius
