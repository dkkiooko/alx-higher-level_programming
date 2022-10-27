#!/usr/bin/python3
import sys
"""script that adds all arguments to local json file
"""


save_json = __import__("5-save_to_json_file").save_to_json_file
load_json = __import__("6-load_from_json_file").load_from_json_file

file_name = "add_item.json"
try:
    new = load_json(file_name)
except Exception:
    new = []
for args in sys.argv[1:]:
    new.append(args)
save_json(new, file_name)
