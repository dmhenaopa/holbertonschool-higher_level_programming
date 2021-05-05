#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    for index in reversed(range(length + 1)):
        print("{:d}".format(my_list[index]))
