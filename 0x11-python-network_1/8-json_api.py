#!/usr/bin/python3
""" takes in a letter and sends a POST to URL with letter param """
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 1:
        q = ''
    else:
        q = argv[1]

    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        respond = r.json()
        if respond:
            print('[{}] {}'.format(respond['id'], respond['name']))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
