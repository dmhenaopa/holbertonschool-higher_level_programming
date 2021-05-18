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

    def __init__(self, size):
        """__init__ method to initialize the Square
           instance with a size

           Args:
                param1 (size): Size of square object (private)
        """
        self.__size = size
