#!/usr/bin/python3
import sys
from sys import exc_info


def safe_function(fct, *args):
    try:
        r = fct(args[0], args[1])
    except:
        print("Exception: {}".format(exc_info()[1]), file=sys.stderr)
        r = None
    return r
