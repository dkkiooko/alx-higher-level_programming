#!/usr/bin/python3
""" Error code detection """
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == '__main__':
    req = Request(argv[1])
    try:
        with urlopen(req) as f:
            response = f.read()
            print(response.decode('utf8'))
    except HTTPError as e:
        print("Error code:", e.code)
