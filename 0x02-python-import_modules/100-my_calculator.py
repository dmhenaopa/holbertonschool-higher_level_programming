#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    # Verify number of arguments is equal to 4 - with command
    if len(sys.argv) != 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    symbol = sys.argv[2]

    if symbol == '+' or symbol == '-' or symbol == '*' or symbol == '/':
        if sys.argv[2] == '+':
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

        elif sys.argv[2] == '-':
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))

        elif sys.argv[2] == '*':
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))

        else:
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

    else:
        print("{}{}".format("Unknown operator. ",
                            "Available operators: +, -, * and /"))
        exit(1)
