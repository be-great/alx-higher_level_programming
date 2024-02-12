#!/usr/bin/python3
""" Module : unittests for Rectangle class."""

import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
import models.rectangle as filename
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Class: define unittests for class Rectangle"""

    def setUp(self):
        """setUp"""
        Base._Base__nb_objects = 0

    def test_file_doc(self):
        """Test doc"""
        self.assertIsNotNone(Rectangle.__doc__)

    def test_class_doc(self):
        """Test doc"""
        self.assertIsNotNone(filename.__doc__)

    def test_construct_doc(self):
        """Test doc"""
        self.assertIsNotNone(Rectangle.__init__.__doc__)

    def test_area_doc(self):
        """Test doc"""
        self.assertIsNotNone(Rectangle.area.__doc__)

    def test_display_doc(self):
        """Test doc"""
        self.assertIsNotNone(Rectangle.display.__doc__)

    def test_str_doc(self):
        """Test doc"""
        self.assertIsNotNone(Rectangle.__str__.__doc__)

    def test_update_doc(self):
        """Test doc"""
        self.assertIsNotNone(Rectangle.update.__doc__)

    def test_width_doc(self):
        """Test doc"""
        self.assertIsNotNone(Rectangle.width.__doc__)

    def test_height_doc(self):
        """Test doc"""
        self.assertIsNotNone(Rectangle.height.__doc__)

    def test_x_doc(self):
        """Test doc"""
        self.assertIsNotNone(Rectangle.x.__doc__)

    def test_y_doc(self):
        """Test doc"""
        self.assertIsNotNone(Rectangle.y.__doc__)

    def test_to_dictionary_doc(self):
        """Test doc"""
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)

    def test_first_id(self):
        """Test id"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def test_second_id(self):
        """Test id"""
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 1)

    def test_giving_id(self):
        """Test id with argument"""
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_third_id(self):
        """Test id"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def test_invalid_height(self):
        """Test type"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_invalid_width(self):
        """Test type"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_invalid_neg_width(self):
        """Test type"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(10, 2)
            r.width = -10

    def test_invalid_neg_height(self):
        """Test type"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(10, 2)
            r.height = -10

    def test_invalid_x(self):
        """Test type"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 2)
            r.x = {}

    def test_invalid_y(self):
        """Test type"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 2)
            r.y = {}

    def test_negative_y(self):
        """Test type"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_negative_x(self):
        """Test type"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -3, 1)

    def test_area_0(self):
        """Test area_0"""
        r1 = Rectangle(10, 2)
        area = r1.area()
        self.assertEqual(area, 20)

    def test_area_1(self):
        """Test area_1"""
        r1 = Rectangle(8, 7, 0, 0, 12)
        area = r1.area()
        self.assertEqual(area, 56)

    def test_display_0(self):
        """
        Test display_0
        with (x, y) = (0, 0)
        """
        r5 = Rectangle(4, 6)

        # capture the printed ouput with stringio and mock
        with patch('sys.stdout', new_callable=StringIO) as mc:
            r5.display()
            output = mc.getvalue().strip()

        expected_out = "####\n####\n####\n####\n####\n####"
        self.assertEqual(output, expected_out)

    def test_display_1(self):
        """
        Test display_1
        with (x, y) = (0, 0)
        """
        r5 = Rectangle(2, 2)

        # capture the printed ouput with stringio and mock
        with patch('sys.stdout', new_callable=StringIO) as mc:
            r5.display()
            output = mc.getvalue().strip()

        expected_out = "##\n##"
        self.assertEqual(output, expected_out)

    def test_str_0(self):
        """Test __str__: 0"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_1(self):
        """Test __str__ : 1"""
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_display_2(self):
        """
        Test display_2
        with (x, y) = (2, 2)
        """
        r3 = Rectangle(2, 3, 2, 2)

        # capture the printed ouput with stringio and mock
        with patch('sys.stdout', new_callable=StringIO) as mc:
            r3.display()
            output = mc.getvalue().strip()

        expected_out = "##\n  ##\n  ##"
        self.assertEqual(output, expected_out)

    def test_display_3(self):
        """
        Test display_3
        with (x, y) = (1, 0)
        """
        r4 = Rectangle(3, 2, 1, 0)

        # capture the printed ouput with stringio and mock
        with patch('sys.stdout', new_callable=StringIO) as mc:
            r4.display()
            output = mc.getvalue().strip()

        expected_out = "###\n ###"
        self.assertEqual(output, expected_out)

    def test_update_0(self):
        """Test update_0"""
        r5 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r5), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_1(self):
        """Test update_1"""
        r5 = Rectangle(10, 10, 10, 10)
        r5.update(89)
        self.assertEqual(str(r5), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_2(self):
        """Test update_2"""
        r5 = Rectangle(10, 10, 10, 10)
        r5.update(89, 2)
        self.assertEqual(str(r5), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_3(self):
        """Test update_3"""
        r5 = Rectangle(10, 10, 10, 10)
        r5.update(89, 2, 3)
        self.assertEqual(str(r5), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_4(self):
        """Test update_4"""
        r5 = Rectangle(10, 10, 10, 10)
        r5.update(89, 2, 3, 4)
        self.assertEqual(str(r5), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_5(self):
        """Test update_5"""
        r5 = Rectangle(10, 10, 10, 10)
        r5.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r5), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_6(self):
        """
        Test update_6
        with kwargs
        """
        r5 = Rectangle(10, 10, 10, 10)
        r5.update(height=1)
        self.assertEqual(str(r5), "[Rectangle] (1) 10/10 - 10/1")
        r5.update(width=1, x=2)
        self.assertEqual(str(r5), "[Rectangle] (1) 2/10 - 1/1")
        r5.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r5), "[Rectangle] (89) 3/1 - 2/1")
        r5.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r5), "[Rectangle] (89) 1/3 - 4/2")

    def test_to_dictionary(self):
        """ returns the dictionary representation of a Rectangle"""
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(r1.to_dictionary(),
                         {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})
        self.assertIsInstance(r1.to_dictionary(), dict)

    def test_update_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_update_kwargs_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def test_update_kwargs_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/6 - 2/4", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_kwargs_some_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))


if __name__ == '__main__':
    unittest.main()
