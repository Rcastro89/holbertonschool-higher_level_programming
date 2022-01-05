#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    if matrix:
        for i in matrix:
            fila = []
            for k in i:
                fila.append(k * k)
            new_matrix.append(fila)
    return new_matrix
