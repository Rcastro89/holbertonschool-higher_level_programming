#!/usr/bin/python3
"""write file"""


def write_file(filename="", text=""):
    """write file again"""
    
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)
