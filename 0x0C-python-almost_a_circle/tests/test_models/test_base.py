#!/usr/bin/python3
""" Module : unittests for Base class."""

import unittest
from models.base import Base
import models.base as filename
from models.rectangle import Rectangle
from models.square import Square
import json
import os
import pep8


class TestBase(unittest.TestCase):
    """Class: define unittests for class Base"""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
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

    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

    """class TestBase"""
    def test_id(self):
        """check id"""
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertIsNotNone(id(b1))

    def test_init(self):
        """check instance"""
        Base._Base__nb_objects = 0
        b2 = Base()
        self.assertIsInstance(b2, Base)

    def test_numObj(self):
        """check number of objects"""
        Base._Base__nb_objects = 0
        b3 = Base()
        self.assertEqual(b3.id, 1)

    def test_toJsonString(self):
        """check to_json_string"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        a_dict = r1.to_dictionary()  # dict
        json_string = json.dumps([a_dict])  # str of list dict
        json_listdict = r1.to_json_string([a_dict])  # str of list dict
        self.assertTrue(json_string == json_listdict)

    def test_saveToFile(self):
        """check save_to_file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        a_dict = [r1.to_dictionary(), r2.to_dictionary()]  # list dict
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            list_dict = json.loads(file.read())  # list dict
        self.assertTrue(a_dict == list_dict)

    def test_fromJsonString(self):
        """check from_json_string"""
        Base._Base__nb_objects = 0
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]  # list dict
        json_list_input = Rectangle.to_json_string(list_input)  # str list dict
        list_output = Rectangle.from_json_string(json_list_input)  # list dict
        self.assertTrue(list_input == list_output)

    def test_create(self):
        """check create"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_loadFromFile(self):
        """check load from file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertTrue(type(list_rectangles_output) == list)
        for rect in list_rectangles_input:
            self.assertTrue(isinstance(rect, Rectangle))
        for rect in list_rectangles_output:
            self.assertTrue(isinstance(rect, Rectangle))
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertTrue(type(list_squares_output) == list)
        for sqr in list_squares_input:
            self.assertTrue(isinstance(sqr, Square))
        for sqr in list_squares_output:
            self.assertTrue(isinstance(sqr, Square))

    def test_pep8_model(self):
        """tests for pep8"""
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_test(self):
        """tests for pep8"""
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


if __name__ == '__main__':
    unittest.main()
