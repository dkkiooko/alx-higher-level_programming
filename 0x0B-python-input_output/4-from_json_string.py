#!/usr/bin/python3
import json
"""load json object from string
"""


def from_json_string(my_str):
    """turn string into json object

    Args:
        my_str (_str_): string with key value pairs or list

    Returns:
        _json_: _a json object in key value pairs_
    """
    return json.loads(my_str)
