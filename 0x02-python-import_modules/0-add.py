#!/usr/bin/python3
import add_0
if __name__ == "__main__":
    # This only run when is not called via 'import'
    a = 1
    b = 2

    value = add_0.add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, value))
