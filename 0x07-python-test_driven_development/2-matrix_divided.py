#!/usr/bin/python3
"""
   matrix_divided module:

   This module contain a method (matrix_divided())
   to divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
       Method to divide the elements of a matrix by a number

       Args:
            param1 (matrix): A list of lists of float or int numbers
            param 2 (div): The number which it is going to be divided
    """
    copy = []
    row_lenght = 0

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    else:
        if div == 0:
            raise ZeroDivisionError("division by zero")

        else:
            """Comprobate is a list"""
            if type(matrix) is not list or not matrix:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers"
                                "/floats")

            for i in range(len(matrix)):
                if type(matrix[i]) is not list or not matrix[i]:
                    raise TypeError("matrix must be a matrix "
                                    "(list of lists) of "
                                    "integers/floats")

                row_lenght = len(matrix[0])
                if row_lenght != len(matrix[i]):
                    raise TypeError("Each row of the matrix "
                                    "must have the same size")
                row = []
                for j in range(len(matrix[i])):
                    if (type(matrix[i][j]) is not int and
                       type(matrix[i][j]) is not float):
                        raise TypeError("matrix must be a matrix "
                                        "(list of lists) of "
                                        "integers/floats")

                    row.append(round((matrix[i][j]/div), 2))
                copy.append(row)

    return copy
