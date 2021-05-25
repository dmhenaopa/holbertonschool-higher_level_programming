#!/usr/bin/python3
"""
   add_integer module:

   This module contain a method (add_integer())
   to add two integer numbers
"""


def add_integer(a, b=98):
    """
    Method to add two numbers as integers

    Args:
         param1 (a): Number 1 (could be float)
         param2 (b): Number 2 (could be float too)
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')

    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')

    else:
        add = int(a) + int(b)
        return add
