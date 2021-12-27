#!/usr/bin/python3
import sys
if __name__ == '__main__':
    k = 0
    for i in sys.argv:
        k = k + 1
    if k == 1:
        print("0 arguments.")
    elif k == 2:
        print("1 argument:")
        print("1: {:s}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(k - 1))
        j = 1
        for i in sys.argv:
            if j < k:
                print("{:d}: {:s}".format(j, sys.argv[j]))
                j = j + 1
