#!/usr/bin/python3
""" error codes """
import requests
from sys import argv


if __name__ == '__main__':
    try:
        req = requests.get(argv[1])
        if req:
            print(req.content.decode('utf-8'))
        elif req.status_code >= 400:
            print("Error code: {}".format(req.status_code))
    except Exception:
        pass
