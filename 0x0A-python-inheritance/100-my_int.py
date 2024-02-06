#!/usr/bin/python3

"""
class MyInt that inherits from int:
"""


class MyInt(int):
    """
    args: (superparent) int
    Discription : MyInt has == and != operators inverted
    """

    def __eq__(self, other):
        """check if the value is not equal"""
        return self.real != other

    def __ne__(self, other):
        """check if the value is equal"""
        return self.real == other
