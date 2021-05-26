#!/usr/bin/python3
"""
   say_my_name module:

   This module contain a method (say_my_name())
   to print two strings - first and last names
"""


def say_my_name(first_name, last_name=""):
    """
       Method to print the first and last name

       Args:
            param1 (first_name): The first name - string
            param2 (last_name): The last name - string
    """
    if type(first_name) is not str or first_name is None:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    else:
        print("My name is {} {}".format(first_name, last_name))
