#!/usr/bin/python3
"""
function that draw a square with symboles.
"""


def print_square(size):
    """function that print square"""
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
