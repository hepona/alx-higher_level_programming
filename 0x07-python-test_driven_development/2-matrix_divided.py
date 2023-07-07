#!/usr/bin/python3
"""
This is a simple module that provides a function that divide matrix.
"""


def matrix_divided(matrix, div):
    """function that divid matrix"""
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        for j in range(len(matrix)):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError(
                    "matrix must be a \
matrix (list of lists) of integers/floats"
                )
    ln = len(matrix[0])
    for i in matrix:
        if len(i) != ln:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    nw = []
    for i in matrix:
        r = []
        for j in i:
            r.append(round(j / div, 2))
        nw.append(r)
    return nw
