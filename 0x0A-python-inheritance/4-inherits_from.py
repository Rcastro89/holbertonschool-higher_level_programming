#!/usr/bin/python3
"""Validate subclass"""


def inherits_from(obj, a_class):
    """inherist from"""

    return (issubclass(type(obj), a_class) if type(obj) != a_class else False)
