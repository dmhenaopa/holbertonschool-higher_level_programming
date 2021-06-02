#!/usr/bin/python3
"""Module that have the lookup function"""


def lookup(obj):
    """Function that returns the list of available attributes
       and methods of an object

       Args:
            param1 (obj): The object
    """
    return dir(obj)
