#!/usr/bin/python3
"""Function that returns an object"""
import json


def from_json_string(my_str):
    """
       Function that returns an object (Python data
       structure) represented by a JSON string

       Args:
            param1 (my_str): String - object
    """
    python_representation = json.loads(my_str)
    return python_representation
