#!/usr/bin/python3
"""Module with a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
       Function that finds a peak in a list of unsorted integers

       Args:
           param1 (list_of_integers): list of unsorted integers
    """
    if list_of_integers:
        return max(list_of_integers)
    else:
        return None
