#!/usr/bin/python3
"""module that prints 2 new lines after characters"""


def text_indentation(text):
    """prints 2 new lines after .?:

    Args:
        text (string): string to modify

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    symbols = ['.', '?', ':']
    idx = 0
    for items in text:
        if items in symbols:
            if text[idx + 1] == " ":
                text = text[:idx + 1] + text[idx + 2:]
        else:
            idx += 1

    idx = 0
    for items in text:
        if items in symbols:
            text = text[:idx + 1] + '\n\n' + text[idx + 1:]
            idx += 3
        else:
            idx += 1

    print(text, end='')
