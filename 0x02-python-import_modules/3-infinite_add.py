#!/usr/bin/python3
import sys
if __name__ == '__main__':
    a = 1
    b = 0
    large = len(sys.argv) - 1
    for i in sys.argv:
        if a <= large:
            b = b + int(sys.argv[a])
            a = a + 1
    print(b)
