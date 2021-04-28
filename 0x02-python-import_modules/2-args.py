#!/usr/bin/python3
import sys
if __name__ == "__main__":
    counter = 0
    number_arguments = len(sys.argv) - 1

    if number_arguments == 0:
        print("{:d} arguments.".format(number_arguments))

    elif number_arguments == 1:
        print("{:d} argument:".format(number_arguments))

    else:
        print("{:d} arguments:".format(number_arguments))

    for arg in sys.argv:
        if counter < number_arguments:
            counter = counter + 1
            print("{:d}: {}".format(counter, sys.argv[counter]))
