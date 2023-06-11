#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 or matrix is None:
        return print("")
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print("{:d}".format(matrix[i][j]), end=" "
                  if j != len(matrix) - 1 else "")
        print()
