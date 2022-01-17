#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        r = fct(args[0], args[1])
    except (ZeroDivisionError, IndexError, TypeError, ValueError) as e:
        print("Exception: {}".format(str(e)), file=sys.stderr)
        r = None
    return r
