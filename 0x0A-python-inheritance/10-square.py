#!/usr/bin/python3
"""define BaseGeometry class"""


class BaseGeometry:
    """define it's attribute"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
        return value


"""define Rectangle class"""


class Rectangle(BaseGeometry):
    """define it's attribute"""

    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


"""define Square Class"""


class Square(Rectangle):
    """define it's attribute"""

    def __init__(self, size):
        self.__size = self.integer_validator("size", size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
