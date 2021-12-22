#!/usr/bin/env python3
def print_last_digit(number):
    if number > -1:
        lastdigit = number % 10
    else:
        lastdigit = ((number * -1) % 10) * -1
    lastdigit = int(repr(number)[-1])
    print("{:d}".format(lastdigit), end="")
    return lastdigit
