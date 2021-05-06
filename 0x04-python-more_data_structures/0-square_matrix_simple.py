#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    length = len(matrix)

    for i in range(0, len(matrix)):
        for j in range(0, 3):
            new_list.append(matrix[i][j] ** 2)

    new_mat = [new_list[x:x+length] for x in range(0, len(new_list), length)]
    return new_mat
