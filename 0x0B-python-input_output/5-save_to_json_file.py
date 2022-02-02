#!/usr/bin/python3
"""save to json"""

import json


def save_to_json_file(my_obj, filename):
    """save to json again"""

    jsonstring = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as my_file:
        my_file.write(jsonstring)
