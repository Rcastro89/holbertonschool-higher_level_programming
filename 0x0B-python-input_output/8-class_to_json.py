#!/usr/bin/python3
"""class to json"""

import json


def class_to_json(obj):
    """return class"""
    return obj.__dict__
