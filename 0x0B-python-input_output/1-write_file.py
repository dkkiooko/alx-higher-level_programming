#!/usr/bin/python3
"""module that writes file"""


def write_file(filename="", text=""):
    """writes file into computer location

    Args:
        filename (str, optional): _path on computer_. Defaults to "".
        text (str, optional): text to be written on computer. Defaults to "".

    Returns:
        _int_: _number of charactes in text_
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
