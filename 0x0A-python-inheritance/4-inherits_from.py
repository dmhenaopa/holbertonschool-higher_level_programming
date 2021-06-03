#!/usr/bin/python3
"""Module that contains the function inherits_from"""


def inherits_from(obj, a_class):
    """
       Function that verify if the object is an instance of a
       class that inherited (directly or indirectly) from the
       specified class

       Args:
            param1 (obj): The object to verify
            param2 (a_class): The specified class
    """
    if type(obj) is not a_class:
        return True
    else:
        return False
