#!/usr/bin/python3
"""Module that have the is kind of class function"""


def is_kind_of_class(obj, a_class):
    """
       Function that verifies if the object is an instance of,
       or the object is an instance of a class that inherited from,
       the specified class.

       Args:
            param1 (obj): The object to verify
            param2 (a_class): The specified class
    """
    if isinstance(obj, a_class):
        return True

    else:
        return False
