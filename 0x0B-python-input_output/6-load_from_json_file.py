#!/usr/bin/python3
"""load from json"""

import json


def load_from_json_file(filename):
    """load from json"""

    with open(filename, "r") as my_file:
        return json.load(my_file)
