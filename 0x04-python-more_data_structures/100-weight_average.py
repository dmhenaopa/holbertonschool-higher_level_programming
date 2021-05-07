#!/usr/bin/python3
def weight_average(my_list=[]):
    sumatory = 0
    dividendo = 0
    average = 0
    if my_list:
        for my_tuple in my_list:
            sumatory = sumatory + (my_tuple[0] * my_tuple[1])
            dividendo = dividendo + (my_tuple[1])
        average = sumatory / dividendo
        return average

    return average
