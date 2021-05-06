#!/usr/bin/python3
def no_c(my_string):
    my_new_string = ''

    for s in my_string:
        if s == 'c' or s == 'C':
            continue

        else:
            my_new_string = my_new_string + s

    return my_new_string
