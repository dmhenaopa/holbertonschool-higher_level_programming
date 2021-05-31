#!/usr/bin/python3


def write_file(filename="", text=""):
    """Function that writes a string to a text file

       Args:
            param1 (filename): Path to file
            param2 (text): string to write in the file
    """
    with open(filename, mode='w', encoding='utf-8') as my_file:
        number_char = my_file.write(text)
        return number_char
