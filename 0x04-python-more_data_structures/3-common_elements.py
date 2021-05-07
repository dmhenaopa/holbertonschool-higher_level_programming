#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_list = []

    for elem1 in set_1:
        for elem2 in set_2:
            if elem1 == elem2:
                common_list.append(elem1)
            else:
                continue
    return common_list
