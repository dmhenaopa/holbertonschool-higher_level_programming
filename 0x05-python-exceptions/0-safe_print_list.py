#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    elements_printed = 0

    for i in range(0, x):
        try:
            print('{}'.format(my_list[i]), end='')
            elements_printed += 1

        except IndexError as err:
            break

        except TypeError as exc:
            break

    print()
    return elements_printed
