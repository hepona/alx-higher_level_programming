#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_c = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix_c.append(pow(matrix[i][j], 2))
    return matrix_c
