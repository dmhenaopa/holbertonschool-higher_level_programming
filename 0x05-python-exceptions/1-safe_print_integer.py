#!/usr/bin/python3


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True

    except TypeError as exc:
        return False

    except ValueError as err:
        return False
