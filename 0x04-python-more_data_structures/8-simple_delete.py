#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    exist = key in a_dictionary

    if exist is True:
        del a_dictionary[key]

    return a_dictionary
