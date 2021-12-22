#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = int(repr(number)[-1])
if lastdigit > 5:
	print("Last digit of {:d} is {:d} and is greater than 5".format(number, lastdigit))
elif lastdigit <= 5 and  lastdigit != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, lastdigit))
else:
    print("Last digit of {:d} is {:d} and is 0".format(number, lastdigit))
