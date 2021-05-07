#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_elements = []

    for elem_1 in set_1:
        if elem_1 not in set_2:
            diff_elements.append(elem_1)

    for elem_2 in set_2:
        if elem_2 not in set_1:
            diff_elements.append(elem_2)

    diff_elements.sort()
    return diff_elements
