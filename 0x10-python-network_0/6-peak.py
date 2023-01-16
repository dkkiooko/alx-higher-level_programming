#!/usr/bin/python3
""" find peak in a list of unsorted integers """

def find_peak(list_of_integers):
    """ finds the highest in a list of integers """
    if len(list_of_integers) == 0:
        return
    else:
        return list_of_integers.sort()[0]
