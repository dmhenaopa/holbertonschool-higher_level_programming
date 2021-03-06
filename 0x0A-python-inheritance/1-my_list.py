#!/usr/bin/python3
"""Module that contains the class MyList"""


class MyList(list):
    """
       Class MyList that has a method to sort the list

       Attributes:
       list: As an external argument
    """
    def print_sorted(self):
        """
           Method to sort and prints the list in ascending order
        """
        new_list = self[:]
        new_list.sort()
        print(new_list)
