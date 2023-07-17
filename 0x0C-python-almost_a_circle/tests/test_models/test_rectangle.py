#!/usr/bin/python3
"""Unittest for Class Rectangle([..])
"""
import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test init with id attribute, is always an integer"""

    def test_init_with_id(self):
        r = Rectangle()
        self.assertEqual(r.id, 1)

    def test_init_without_id(self):
        """Test init without id attribute."""
        obj = Base()
        self.assertIsNotNone(obj.id)
