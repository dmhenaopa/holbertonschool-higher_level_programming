#!/usr/bin/python3
def safe_print_division(a, b):
    result_division = 0

    try:
        result_division = a / b

    except ZeroDivisionError:
        result_division = None

    finally:
        print("Inside result: {}".format(result_division))
        return result_division
