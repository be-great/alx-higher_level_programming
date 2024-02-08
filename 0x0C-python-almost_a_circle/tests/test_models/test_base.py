#!/usr/bin/python3
""" Module : unittests for Base class."""

import unittest
from models.base import Base
import models.base as filename
class TestMaxInteger(unittest.TestCase):
    """Class: define unittests for class Base"""

    def test_file_doc(self):
        """Test doc"""
        self.assertIsNotNone(Base.__doc__)

    def test_class_doc(self):
        """Test doc"""
        self.assertIsNotNone(filename.__doc__)
    def test_construct_doc(self):
        """Test doc"""
        self.assertIsNotNone(Base.__init__.__doc__)
    def test_first_id(self):
        """Test id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
    def test_second_id(self):
        """Test id"""
        b1 = Base()
        self.assertEqual(b1.id, 2)
    def test_giving_id(self):
        """Test id with argument"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_third_id(self):
        """Test id with argument"""
        b1 = Base()
        self.assertEqual(b1.id, 3)





if __name__ == '__main__':
    unittest.main()
