#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """read file again"""

    with open(filename, "r", encoding="utf-8") as files:
        for i in files:
            print(i, end="")
        print()
