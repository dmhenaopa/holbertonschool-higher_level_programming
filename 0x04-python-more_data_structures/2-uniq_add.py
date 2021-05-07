#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    sumatory = 0
    for number in my_list:
        if number not in unique:
            unique.append(number)

    for u_number in unique:
        sumatory = sumatory + u_number

    return sumatory
