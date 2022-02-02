#!/usr/bin/python3
"""append"""


def append_write(filename="", text=""):
    """apped again"""

    with open(filename, "a", encoding="utf-8") as my_file:
        return my_file.write(text)
