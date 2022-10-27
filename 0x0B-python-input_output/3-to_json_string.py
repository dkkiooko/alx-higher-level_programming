#!/usr/bin/python3
import json
"""turns object into json string
"""


def to_json_string(my_obj):
    """returns json string

    Args:
        my_obj (_object_): could be a dict or list

    Returns:
        _str_: a string format of json
    """
    return json.dumps(my_obj)
