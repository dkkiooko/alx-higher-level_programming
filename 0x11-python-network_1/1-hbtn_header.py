#!/usr/bin/python3
""" script fetches header """
from urllib.request import Request, urlopen
from sys import argv


if __name__ == '__main__':
    html = Request(argv[1])
    with urlopen(html) as response:
        header = response.info()
        print(header['X-Request-Id'])
