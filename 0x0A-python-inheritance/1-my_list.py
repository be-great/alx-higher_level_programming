#!/usr/bin/python3
"""
 class MyList that inherits from list
"""


class MyList(list):
    """
    args : list
    """

    def __init__(self, *args):
        super().__init__(args)

    def print_sorted(self):
        """print the lists"""
        print(sorted(self))
