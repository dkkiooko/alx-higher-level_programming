#!/usr/bin/python3
""" POST """
from urllib.request import Request, urlopen
from sys import argv
import urllib.parse


if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    email = data.encode('ascii')
    request = Request(url, email)
    with urlopen(request) as response:
        body = response.read()
        print(body.decode('utf8'))
