#!/usr/bin/python3
import sys
if __name__ == "__main__":
    counter = 0
    sumatory = 0
    number_arguments = len(sys.argv) - 1

    if number_arguments == 0:
        print("{:d}".format(number_arguments))

    else:
        for arg in sys.argv:
            if counter < number_arguments:
                counter = counter + 1
                sumatory = sumatory + int(sys.argv[counter])
        print("{:d}".format(sumatory))
