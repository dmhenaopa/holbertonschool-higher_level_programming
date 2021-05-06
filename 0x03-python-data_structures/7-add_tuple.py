#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length_a = len(tuple_a)
    length_b = len(tuple_b)

    new_tuple = (0, 0)
    if length_a >= 2 and length_b >= 2:
        new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    else:
        if length_a == 2 and length_b == 1:
            new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)

        elif length_a == 2 and length_b == 0:
            new_tuple = (tuple_a[0] + 0, tuple_a[1] + 0)

        elif length_a == 1 and length_b == 2:
            new_tuple = (tuple_a[0] + tuple_b[0], 0 + tuple_b[1])

        elif length_a == 1 and length_b == 1:
            new_tuple = (tuple_a[0] + tuple_b[0], 0 + 0)

        elif length_a == 1 and length_b == 0:
            new_tuple = (tuple_a[0] + 0, 0 + 0)

        elif length_a == 0 and length_b == 2:
            new_tuple = (0 + tuple_b[0], 0 + tuple_b[1])

        elif length_a == 0 and length_b == 1:
            new_tuple = (0 + tuple_b[0], 0 + 0)

        elif length_a <= 0 and length_b <= 0:
            new_tuple = (0 + 0, 0 + 0)

    return new_tuple
