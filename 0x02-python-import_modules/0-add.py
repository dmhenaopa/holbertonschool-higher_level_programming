#!/usr/bin/python3
import add_0 as function_add
if __name__ == "__main__":
    # This only run when is not called via 'import'
    a = 1
    b = 2

    print("{:d} + {:d} = {:d}".format(a, b, function_add.add(a, b)))
