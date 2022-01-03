#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    large_a = len((tuple_a))
    large_b = len((tuple_b))
    if large_a == 0:
        number_a = 0
        number_b = 0
    elif large_a == 1:
        number_a = tuple_a[0]
        number_b = 0
    else:
        number_a = tuple_a[0]
        number_b = tuple_a[1]
    if large_b == 0:
        number_c = 0
        number_d = 0
    elif large_b == 1:
        number_c = tuple_b[0]
        number_d = 0
    else:
        number_c = tuple_b[0]
        number_d = tuple_b[1]
    numberret_a = number_a + number_c
    numberret_b = number_b + number_d
    new_tuple = (numberret_a, numberret_b)
    return new_tuple
