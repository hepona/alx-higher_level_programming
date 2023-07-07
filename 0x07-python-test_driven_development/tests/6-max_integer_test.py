#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    def test_maxinteger(self):
        # test max int
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([10, 2, 3, 4]), 10)
        self.assertAlmostEqual(max_integer([1, -2, 7, 4]), 7)
        self.assertAlmostEqual(max_integer([0.1, 2.79, 3.666, -10.9]), 3.666)
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertAlmostEqual(max_integer([]), None)
        

