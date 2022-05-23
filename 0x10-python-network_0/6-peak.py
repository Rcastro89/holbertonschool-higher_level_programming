#!/usr/bin/python3
"""modeulo to fidn peak"""


def find_peak(list_of_integers):
    """funtion to found peak"""
    numer = None
    if list_of_integers:
        list_of_integers.sort()
        numer = list_of_integers[-1]
    return numer
