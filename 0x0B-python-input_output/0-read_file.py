#!/usr/bin/python3
"""module that reads file"""


def read_file(filename=""):
    """reads file

    Args:
        filename (str, optional): _location of file on comp_. Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as f:
        for line in f.read():
            print(line, end="")
