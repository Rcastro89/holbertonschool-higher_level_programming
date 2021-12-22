#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > -1:
    lastdigit = number % 10
else:
    lastdigit = ((number * -1) % 10) * -1
if lastdigit == 0:
    print('lastdigit digit of {:d} is {:d} and is 0'.format(number, lastdigit))
elif lastdigit > 5:
    print('lastdigit digit of {:d} is {:d} and is greater than 5'
          .format(number, lastdigit))
else:
    print('lastdigit digit of {:d} is {:d} and is less than 6 and not 0'
          .format(number, lastdigit))
