#!/usr/bin/python3
"""Function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """
       Function that creates an Object from a “JSON file”

       Args:
            param1 (filename): JSON file
    """
    with open(filename, mode='r') as json_file:
        data_json = json.load(json_file)
        return data_json
