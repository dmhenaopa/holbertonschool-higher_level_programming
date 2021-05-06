#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []

    if my_list:
        for number in my_list:
            if number % 2 == 0:
                new_list = new_list + [True]

            elif number % 2 != 0:
                new_list = new_list + [False]

    else:
        return None

    return new_list
