#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == '__main__':
    large = len(sys.argv)
    if large != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator = sys.argv[2]
        if (operator != '+' and operator != '-' and
                operator != '*' and operator != '/'):
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            if operator == '+':
                print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
            elif operator == '-':
                print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
            elif operator == '*':
                print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
            else:
                print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
