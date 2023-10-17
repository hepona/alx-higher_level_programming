#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_c = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(pow(matrix[i][j], 2))
        matrix_c.append(row)
    return matrix_c
