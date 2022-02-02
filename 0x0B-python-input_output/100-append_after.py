#!/usr/bin/python3
"""append lines"""


def append_after(filename="", search_string="", new_string=""):
    """append conditional"""
    with open(filename, "r", encoding="utf-8") as files:
        new_file = ""
        read_file = files.readlines()
        for lines in read_file:
            new_file = new_file + lines
            if search_string in lines:
                new_file = new_file + new_string
    files.close()
    with open(filename, "w", encoding="utf-8") as files:
        files.write(new_file)
