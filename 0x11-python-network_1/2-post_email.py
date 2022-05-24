#!/usr/bin/python3
"""Parametre POST
"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    value = {'email': email}
    data = parse.urlencode(value)
    data = data.encode('utf-8')
    with request.urlopen(url, data) as response:
        answer = response.read().decode('utf-8')
    print(answer)
