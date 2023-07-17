#!/usr/bin/python3
"""Unittest for Class Base([..])
"""
import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """Test init with id attribute, is always an integer"""

    def test_init_with_id(self):
        obj = Base(id=1)
        self.assertEqual(obj.id, 1)

    def test_init_without_id(self):
        """Test init without id attribute."""
        obj = Base()
        self.assertIsNotNone(obj.id)
