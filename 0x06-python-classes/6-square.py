#!/usr/bin/python3
"""define a class"""


class Square:
    """define class attribute"""

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if (
            len(position) != 2
            or not isinstance(position[0], int)
            or not isinstance(position[1], int)
            or not position[0] >= 0
            or not position[1] >= 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            len(value) != 2
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or not value[0] >= 0
            or not value[1] >= 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
