#!/usr/bin/python3
""" Module : unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class: define unittests for max_integer([..])."""



    def test_str(self):
        """Test string."""
        self.assertEqual(max_integer("ABCDEF"), 'F')

    def test_str_two(self):
        """Test string two."""
        self.assertEqual(max_integer("F"), 'F')

    def test_list_of_strs(self):
        """Test list of strings."""
        strings = ["Ahed", "Eisa", "number"]
        self.assertEqual(max_integer(strings), "number")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_sorted_list(self):
        """Test sorted list"""
        _list = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(max_integer(_list), 7)

    def test_unsorted_list(self):
        """Test unsorted list"""
        _list = [1, 2, 3, 7, 0]
        self.assertEqual(max_integer(_list), 7)

    def test_max_at_the_start(self):
        """Test max number at the beginning"""
        _list = [7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(max_integer(_list), 7)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test list with one element."""
        self.assertEqual(max_integer([10]), 10)

    def test_nonInterger(self):
        """Test list of None intergers"""
        _list = [0.99, 2.99, -10.9, -15.2222, 6.0]
        self.assertEqual(max_integer(_list), 6.0)

    def test_integer_and_float(self):
        """Test list of integer and float."""
        _list = [0.99, 2.99, -10.9, -15.2222, 6.0]
        self.assertEqual(max_integer(_list), 6.0)

if __name__ == '__main__':
    unittest.main()
