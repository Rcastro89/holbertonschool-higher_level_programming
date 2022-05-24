#!/usr/bin/python3
"""status error
"""
import requests
import sys

if __name__ == '__main__':
    url = requests.get(sys.argv[1])
    err = url.status_code
    print(url.text) if err < 400 else print(
        "Error code: {}".format(url.status_code))
