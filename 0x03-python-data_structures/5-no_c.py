#!/usr/bin/python3
def no_c(my_string):
    x = 0
    new_string = ''
    for i in my_string:
        if my_string[x] != 'c' and my_string[x] != 'C':
            new_string = new_string + my_string[x]
        x += 1
    return new_string
