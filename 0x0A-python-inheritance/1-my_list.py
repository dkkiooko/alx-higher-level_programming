#!/usr/bin/python3
"""module that inherits from list"""


class MyList(list):
    """creates object with attributes from list

    Args:
        list (object): inbuilt Python list module
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """prints MyList obj ascending
        """
        print(sorted(self))
