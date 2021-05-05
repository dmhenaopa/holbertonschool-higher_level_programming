#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)

    if my_list:
        for index in reversed(range(length)):
            print("{:d}".format(my_list[index]))
