#!/usr/bin/python3
from models.base import Base

"""define a class Rectangle"""


class Rectangle(Base):
    """defie it's attribute"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if not (isinstance(width, int)):
            raise TypeError("Width must be an integer")
        if width <= 0:
            raise ValueError("Width must be > 0")
        self.__width = width
        if not (isinstance(height, int)):
            raise TypeError("Height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if not (isinstance(x, int)):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if not (isinstance(y, int)):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not (isinstance(value, int)):
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height should be a positive number")
        if value <= 0:
            raise ValueError("Height cannot be zero or negative.")
        self._height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not (isinstance(value, int)):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y
