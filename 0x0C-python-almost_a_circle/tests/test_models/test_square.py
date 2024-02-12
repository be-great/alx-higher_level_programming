#!/usr/bin/python3
""" Module : unittests for Base class."""

import unittest
from models.square import Square
from models.base import Base
import models.square as filename


class TestSquare(unittest.TestCase):
    """Class: define unittests for class Base"""
    def setUp(self):
        """setUp"""
        Base._Base__nb_objects = 0

    def test_file_doc(self):
        """Test doc"""
        self.assertIsNotNone(Square.__doc__)

    def test_class_doc(self):
        """Test doc"""
        self.assertIsNotNone(filename.__doc__)

    def test_construct_doc(self):
        """Test doc"""
        self.assertIsNotNone(Square.__init__.__doc__)

    def test_str_doc(self):
        """Test doc"""
        self.assertIsNotNone(Square.__str__.__doc__)

    def test_area_str(self):
        """Test area and str"""
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)

    def test_size_getter(self):
        """Test area and str"""
        s1 = Square(5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)

    def test_size_setter(self):
        """Test area and str"""
        s1 = Square(5)
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
        self.assertEqual(s1.width, 10)

    def test_update_func(self):
        """Test area and str"""
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_to_dictionary(self):
        """ returns the dictionary representation of a Rectangle"""
        r1 = Square(10, 2, 1)
        self.assertEqual(r1.to_dictionary(),
                         {'id': 1, 'x': 2, 'size': 10, 'y': 1})
        self.assertIsInstance(r1.to_dictionary(), dict)


if __name__ == '__main__':
    unittest.main()
