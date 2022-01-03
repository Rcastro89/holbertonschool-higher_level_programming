#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        espace = ''
        for k in i:
            print('{}{:d}'.format(espace, k), end='')
            espace = ' '
        print('')
