#!/usr/bin/python3
""" take github credentials and use Github API to display id"""
import requests
from sys import argv


if __name__ == '__main__':
    try:
        r = requests.get("https://api.github.com/user",
                         auth=(argv[1], argv[2]))
        file = r.json()
        print(file['id'])
    except:
        print('None')
