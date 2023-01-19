#!/usr/bin/python3
""" python script """
import urllib.request


if __name__ == '__main__':
    j = urllib.request.urlopen
    with j('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf8')))
