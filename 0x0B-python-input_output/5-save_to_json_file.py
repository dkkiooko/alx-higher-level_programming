#!/usr/bin/python3
import json
"""saves object to json file
"""


def save_to_json_file(my_obj, filename):
    """saves object to file

    Args:
        my_obj (_object_): object in json notation
        filename (_str_): path name to json where to save in location

    Returns:
        _json_: _json object representing written info_
    """
    with open(filename, "w", encoding="utf-8") as f:
        written = json.dump(my_obj, f)
    return written
