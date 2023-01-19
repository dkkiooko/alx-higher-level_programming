#!/usr/bin/python3
""" us variable in request header """
import requests
from sys import argv


if __name__ == "__main__":
    try:
        request = requests.get(argv[1])
        print(request.headers['X-Request-Id'])
    except Exception:
        pass
