#!/usr/bin/python3


def matrix_divided(matrix, div):
    """return new matrix dividided"""
    new_matrix = []
    if (matrix):
        a = len(matrix[0])
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        elif div == 0:
            raise ZeroDivisionError("division by zero")
        for i in matrix:
            fill = []
            if len(i) != a:
                raise TypeError("Each row of the matrix must have the same size")
            for j in i:
                if isinstance(j, (int, float)):
                    fill.append(round(j / div, 2))
                else:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_matrix.append(fill)
    return new_matrix
