#!/usr/bin/python3
"""
   print_square module:

   This module contain a method (print_square())
   to prints a square with the character #.
"""


def print_square(size):
    """
       Method to print a square with the character #

       param1 (size): Size length of the square (integer)
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')

    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for columns in range(0, size):
        for rows in range(0, size):
            print("{}".format("#"), end="")
        print()
