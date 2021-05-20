#!/usr/bin/python3
"""This module contain the Rectangle class and the
   use of attribute as a private attribute
"""


class Rectangle:
    """Class Rectangle that defines a rectangle

       Attributes:
       __width: Private instance attribute
       __height: Private instance attribute
    """
    __height = 0
    __width = 0

    def __init__(self, width=0, height=0):
        """__init__ method to initialize the Rectangle
           instance with a width and height
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter method to width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to width of rectange

           Args:
                param1 (value): Width of rectangle object
        """
        if isinstance(value, int) is False:
            raise TypeError('width must be an integer')

        elif value < 0:
            raise ValueError('width must be >= 0')

        else:
            self.__width = value

    @property
    def height(self):
        """Getter method to height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to height of rectange

           Args:
                param1 (value): Height of rectangle object        """
        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')

        elif value < 0:
            raise ValueError('height must be >= 0')

        else:
            self.__height = value
