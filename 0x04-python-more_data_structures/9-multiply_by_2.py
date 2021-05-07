#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy_dict = a_dictionary.copy()
    for key, value in copy_dict.items():
        copy_dict[key] = value * 2

    return copy_dict
