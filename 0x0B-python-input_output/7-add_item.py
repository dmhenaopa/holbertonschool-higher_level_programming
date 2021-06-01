#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file"""
from sys import argv
from pathlib import Path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

list_arg = []
my_file = "add_item.json"
path = Path(my_file)

if path.is_file():
    """ Create an object from JSON file """
    list_arg = load_from_json_file(my_file)

    for i in range(1, len(argv)):
        """ List of arguments - 1 because the 0 is command """
        list_arg.append(argv[i])

""" Writes an object to a text file """
save_to_json_file(list_arg, my_file)
