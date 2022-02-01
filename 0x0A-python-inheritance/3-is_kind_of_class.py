#!/usr/bin/python3
"""validate subclass"""


def is_kind_of_class(obj, a_class):
    """compare obj whit a_class, validate subclass"""
    return (issubclass(type(obj), a_class))
