#!/usr/bin/python3
""" list last 10 commits """
import requests
from sys import argv


if __name__ == '__main__':
    repo = argv[1]
    owner = argv[2]
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(owner, repo), {'per_page': 10})
    r = r.json()
    for arg in r:
        print("{}: {}".format(arg.get('sha'),
                              arg.get('commit').get('author').get('name')))
