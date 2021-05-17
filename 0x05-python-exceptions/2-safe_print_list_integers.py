#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    elements_printed = 0

    for element in range(0, x):
        try:
            print("{:d}".format(my_list[element]), end="")
            elements_printed += 1

        except TypeError as exc:
            continue

        except ValueError as err:
            continue

    print()
    return elements_printed
