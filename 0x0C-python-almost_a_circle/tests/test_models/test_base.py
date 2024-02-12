#!/usr/bin/python3
""" Module : unittests for Base class."""

import unittest
from models.base import Base
import models.base as filename
from models.rectangle import Rectangle
from models.square import Square
import json
import os


class TestBase(unittest.TestCase):
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

    def test_to_json_string_doc(self):
        """Test doc"""
        self.assertIsNotNone(Base.to_json_string.__doc__)

    def test_save_to_file_doc(self):
        """Test doc"""
        self.assertIsNotNone(Base.save_to_file.__doc__)

    def test_from_json_string_doc(self):
        """Test doc"""
        self.assertIsNotNone(Base.from_json_string.__doc__)

    def test_create_doc(self):
        """Test doc"""
        self.assertIsNotNone(Base.create.__doc__)

    def test_load_from_file_that_have_json_doc(self):
        """Test doc"""
        self.assertIsNotNone(Base.load_from_file.__doc__)

    def test_id(self):
        """Test id"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_giving_id(self):
        """Test id with argument"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_to_json_string(self):
        """Test representation of string to json"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        self.assertIsInstance(dictionary, dict)
        self.assertEqual(dictionary,
                         {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8})
        json_dictionary = json.loads(Base.to_json_string([dictionary]))
        excepted = [{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]
        self.assertEqual(json_dictionary, excepted)

        json_dictionary = Base.to_json_string(None)
        self.assertIsInstance(json_dictionary, str)
        self.assertEqual(json_dictionary, '[]')

    def test_save_to_file(self):
        """Test save json of list_objs to a file """
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertIsInstance(content, str)
            actual = json.loads(content)
            expected = [
                {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
                {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}
            ]

            # Check if the elements are present in the expected order
            self.assertEqual(actual, expected)

    def test_third_id(self):
        """Test id"""
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

        self.assertIsInstance(list_input, list)
        self.assertIsInstance(json_list_input, str)
        self.assertIsInstance(list_output, list)

        # Use json.loads to compare the lists without considering order
        expected_list = [{'id': 89, 'width': 10, 'height': 4},
                         {'id': 7, 'width': 1, 'height': 7}]

        self.assertEqual(json.loads(json_list_input), expected_list)
        self.assertEqual(list_output, expected_list)

    def test_create_(self):
        """returns an instance with all attributes already set"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        # When
        r2 = Rectangle.create(**r1_dictionary)
        # Then
        res = r1 == r2
        self.assertIsInstance(r2, Rectangle)
        self.assertIsNot(r1, r2)  # Ensure different instances
        self.assertEqual(res, False)  # Ensure equal values

    def test_load_from_file(self):
        """Test: the file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output[0]),
                         str(list_rectangles_input[0]))
        self.assertEqual(str(list_rectangles_output[1]),
                         str(list_rectangles_input[1]))
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(list_squares_output[0]),
                         str(list_squares_input[0]))
        self.assertEqual(str(list_squares_output[1]),
                         str(list_squares_input[1]))

    def test_save_and_load_file_csv(self):
        """Test: the file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(list_rectangles_output[0]),
                         str(list_rectangles_input[0]))
        self.assertEqual(str(list_rectangles_output[1]),
                         str(list_rectangles_input[1]))
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(list_squares_output[0]),
                         str(list_squares_input[0]))
        self.assertEqual(str(list_squares_output[1]),
                         str(list_squares_input[1]))


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file__csv_cls_name(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == '__main__':
    unittest.main()
