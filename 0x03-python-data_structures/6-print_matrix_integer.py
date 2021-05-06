#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    number_rows = len(matrix)
    number_col = len(matrix[0])

    for row in range(number_rows):
        for col in range(number_col):
            print("{:d}".format(matrix[row][col]), end="")
            if (col < (number_col - 1)):
                print("{}".format(" "), end="")

        print("{}".format(""))
