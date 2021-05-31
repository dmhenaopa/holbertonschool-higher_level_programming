#!/usr/bin/python3
"""Function that appends a string at the end"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of
       a text file

       Args:
            param1 (filename): Path to file
            param2 (text): String to add
    """
    with open(filename, mode='a', encoding='utf-8') as my_file:
        number_char = my_file.write(text)
        return number_char
