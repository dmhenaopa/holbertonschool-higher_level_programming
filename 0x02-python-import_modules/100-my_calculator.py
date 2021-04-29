#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    # Verify number of arguments is equal to 4 - with command
    if len(argv) != 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    symbol = argv[2]

    if symbol == '+' or symbol == '-' or symbol == '*' or symbol == '/':
        if argv[2] == '+':
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

        elif argv[2] == '-':
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))

        elif argv[2] == '*':
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))

        else:
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

    else:
        print("{}{}".format("Unknown operator. ",
                            "Available operators: +, -, * and /"))
        exit(1)
