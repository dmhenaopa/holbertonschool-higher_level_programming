#!/usr/bin/python3
"""Function that returns the structure for JSON serialization of an object"""


def class_to_json(obj):
    """Function that returns a dictionary containing all
       local variables of the object

       Args:
            param1 (obj): JSON object
    """
    variables = vars(obj)
    return variables
