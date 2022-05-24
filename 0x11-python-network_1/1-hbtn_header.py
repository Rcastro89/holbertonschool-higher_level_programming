#!/usr/bin/python3
"""obtener request id
"""


if __name__ == "__main__":
    import sys
    import urllib.request
    with urllib.request.urlopen(sys.argv[1]) as response:
        headers = response.info()
        print(headers['X-Request-Id'])
