#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = number % 10
if (number > 0):
    if (mod == 0):
        print(f"Last digit of {number:d} is {mod:d} and is 0")
    elif (mod > 5):
        print(f"Last digit of {number:d} is {mod:d} and is greater than 5")
    elif (mod < 6) and (mod != 0):
        print(f"Last digit of {number:d} is"
              f" {mod:d} and is less than 6 an not 0")
else:
    if (mod == 0):
        print(f"Last digit of {number:d} is {-1*mod:d} and is 0")
    elif (mod > 5):
        print(f"Last digit of {number:d} is {-1*mod:d} and is greater than 5")
    elif (mod < 6) and (mod != 0):
        print(f"Last digit of {number:d} is"
              f" {-1*mod:d} and is less than 6 an not 0")
