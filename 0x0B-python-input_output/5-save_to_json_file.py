#!/usr/bin/python3
"""Function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """
       Function that writes an Object to a text file,
       using a JSON representation

       Args:
            param1 (my_obj): The object
            param2 (filename): Path to a text file
    """
    with open(filename, mode='w', encoding='utf-8') as my_file:
        json.dump(my_obj, my_file)
