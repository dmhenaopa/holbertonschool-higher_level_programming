#!/usr/bin/python3


def read_file(filename=""):
    with open(filename, encoding='utf-8') as my_file:
        read_data = my_file.read()
        print("{}".format(read_data), end=" ")
