#!/usr/bin/python3
def uppercase(str):
    for element in str:
        if (97 <= ord(element) <= 122):
            element = chr(ord(element) - 32)
        print(f"{element}", end="")
