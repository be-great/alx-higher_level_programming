#!/usr/bin/python3
"""this is a program that create a node class
and insert to linked list  and print the linked list
"""


class Node:
    """
    args:
        data: the node data
        next_node: the next node
    """

    def __init__(self, data, next_node=None):
        """a private instance attribute"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get the data instance attribute"""

        return self.__data

    @data.setter
    def data(self, value):
        """set the data instance attribute"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get the next instance attribute"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set the data instance attribute"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
        args:
            value : to insert to the head
    """

    def __init__(self):
        """a private instance attribute"""
        self.head = None

    def sorted_insert(self, value):
        """insert to the linked list"""

        new_node = Node(value)
        if self.head is None or self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """the default class string is the linked list"""

        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
