#!/usr/bin/python3
"""
    Represents a rectangle with width, height, position (x, y), and an identifier (id).

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x-coordinate of the top-left corner of the rectangle.
        __y (int): The y-coordinate of the top-left corner of the rectangle.
        id (int): The identifier for the rectangle, inherited from the Base class.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
            Initializes a Rectangle instance with the provided width, height, position, and id.

        width(self):
            Getter method for retrieving the width of the rectangle.

        width(self, value):
            Setter method for setting the width of the rectangle.

        height(self):
            Getter method for retrieving the height of the rectangle.

        height(self, value):
            Setter method for setting the height of the rectangle.

        x(self):
            Getter method for retrieving the x-coordinate of the rectangle's position.

        x(self, value):
            Setter method for setting the x-coordinate of the rectangle's position.

        y(self):
            Getter method for retrieving the y-coordinate of the rectangle's position.

        y(self, value):
            Setter method for setting the y-coordinate of the rectangle's position.
"""
from base import Base


class Rectangle(Base):
    """defie it's attribute"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if not (isinstance(width, int)):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if not (isinstance(height, int)):
            raise TypeError("height must be an integer")
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
        """getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width"""
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >0")
        self.__height = value

    @property
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter x"""
        if not (isinstance(value, int)):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter y"""
        if not (isinstance(value, int)):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
