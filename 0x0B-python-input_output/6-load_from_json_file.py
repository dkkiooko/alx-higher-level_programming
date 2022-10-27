#!/usr/bin/python3
import json
"""load json info from a file
"""


def load_from_json_file(filename):
    """load from a file

    Args:
        filename (_path_): _path to location where file is located_

    Returns:
        _json_: _json representation of content in location_
    """
    with open(filename, "r", encoding="utf-8") as f:
        created = json.load(f)
    return created
