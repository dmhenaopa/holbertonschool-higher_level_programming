#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_copy_list = my_list.copy()
    length = len(my_copy_list)
    if idx < 0 or idx >= length:
        return my_copy_list

    else:
        my_copy_list[idx] = element
        return my_copy_list
