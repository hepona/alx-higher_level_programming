#!/usr/bin/python3
"""Unittest for Class Rectangle([..])
"""
import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test init with all rectangle attribute"""

    def test_init_with_Allattribute(self):
        r = Rectangle(5, 7, 9, 4, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 4)

    def test_init_without_id(self):
        r = Rectangle(5, 7, 9, 4)
        self.assertEqual(r.id, 15)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 4)

    def test_init_with_Width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("a", 7, 9, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("5", 7, 9, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((5, 7, 9), 7, 9, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(("a", "b", "c"), 7, 9, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 7, 9], 7, 9, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.9, 7, 9, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 7, 9, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 7, 9, 4)

    def test_init_with_Height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, "a", 9, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, (5, 7, 9), 9, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, ("a", "b", "c"), 9, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, [1, 7, 9], 9, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, 7.9, 9, 4)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -7, 9, 4)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0, 9, 4)

    def test_init_with_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 9, "a", 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 5, (5, 7, 9), 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 5, ("a", "b", "c"), 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 9, [1, 7, 9], 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 7, 9.6, 4)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 7, -9, 4)

    def test_init_with_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 9, 9, "a")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 5, 4, (5, 7, 9))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 5, 4, ("a", "b", "c"))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 9, 4, [1, 7, 9])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 7, 4, 9.6)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 7, 9, -4)
