#!/usr/bin/python3


def read_file(filename=""):
    """
       Function that reads a text file

       Args:
            param1 (filename): Path to file
    """
    with open(filename, encoding='utf-8') as my_file:
        read_data = my_file.read()
        print("{}".format(read_data), end=" ")
