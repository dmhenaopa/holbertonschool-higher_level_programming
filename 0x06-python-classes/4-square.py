#!/usr/bin/python3
"""This module contain the Square class and the
   use of attribute as a private attribute
"""


class Square():
    """Class square that defines a square

       Attributes:
       __size: Private instance attribute
    """
    __size = 0

    def __init__(self, size=0):
        """__init__ method to initialize the Square
           instance with a size

           Args:
                param1 (size): Size of square object (private)
        """
        self.__size = size

    def area(self):
        """Calculate the current square area

           Returns:
               int: Area of the square
        """
        area = self.__size ** 2
        return area

    @property
    def size(self):
        """Getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method

           Args:
                param1 (value): Size of square object
        """
        if isinstance(value, int) is False:
            raise TypeError('size must be an integer')

        elif value < 0:
            raise ValueError('size must be >= 0')

        else:
            self.__size = value
