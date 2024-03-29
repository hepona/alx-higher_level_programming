#!/usr/bin/python3
"""define a class"""


class Square:
    """define class attribute"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        s = self.__size * self.__size
        return s

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            print("#" * self.__size)
