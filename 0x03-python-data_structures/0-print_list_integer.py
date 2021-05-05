#!/usr/bin/python3
def print_list_integer(my_list=[]):
	lenght = len(my_list)
	for index in range(0, lenght):
            print("{:d}".format(my_list[index]))
