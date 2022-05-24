#!/usr/bin/python3
"""emeail post
"""
import requests
import sys

if __name__ == "__main__":
    print(requests.post(sys.argv[1], data={'email': sys.argv[2]}).text)
