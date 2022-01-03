#!/usr/bin/python3
def max_integer(my_list=[]):
    number_max = 'None'
    if my_list:
        number_max = my_list[0]
        count = len(my_list)
        i = 1
        while i < count:
            if my_list[i] > number_max:
                number_max = my_list[i]
            i += 1
    return number_max
