#!/usr/bin/python3
"""define class Square"""


class Square:
    """define class attribute"""

    def __init__(self, __size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
