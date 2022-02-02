#!/usr/bin/python3
"""save to json"""

import json


def save_to_json_file(my_obj, filename):
    """save to json again"""

    with open(filename, "w", encoding="utf-8") as my_file:
        jsonstring = json.dumps(my_obj)
        my_file.write(jsonstring)
