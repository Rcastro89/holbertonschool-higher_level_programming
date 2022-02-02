#!/usr/bin/python3
"""add item"""
import sys

Ljson = __import__('6-load_from_json_file').load_from_json_file
Sjson = __import__('5-save_to_json_file').save_to_json_file

try:
    list_my = Ljson("add_item.json")
except Exception:
    list_my = []

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        list_my.append(sys.argv[i])
Sjson(list_my, "add_item.json")
