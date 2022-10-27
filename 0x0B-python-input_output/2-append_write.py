#!/usr/bin/python3
"""append to file
"""


def append_write(filename="", text=""):
    """append to file

    Args:
        filename (str, optional): location on computer_. Defaults to "".
        text (str, optional): _text to be appended to file_. Defaults to "".

    Returns:
        _int_: _length of characters writtern_
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
