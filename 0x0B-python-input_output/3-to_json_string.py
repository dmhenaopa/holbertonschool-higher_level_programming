#!/usr/bin/python3
"""Function that return the JSON representation"""
import json


def to_json_string(my_obj):
    """
       Function that returns the JSON representation
       of an object (string)

       Args:
            param1 (my_obj): Object or string
    """
    json_representation = json.dumps(my_obj)
    return json_representation
