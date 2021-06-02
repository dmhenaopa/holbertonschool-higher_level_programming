#!/usr/bin/python3
"""Module that contains the function is_same_class"""


def is_same_class(obj, a_class):
    """
       Function that verifies if the object is exactly an
       instance of the specified class

       Args:
            param1 (obj): The object to verify
            param2 (a_class: The specified class
    """
    if type(obj) is a_class:
        return True

    else:
        return False
