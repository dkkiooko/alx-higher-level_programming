#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for i in range(x):
        try:
            isinstance(my_list[i], int)
            print("{:d}".format(my_list[i]), end= "")
            n += 1
        except IndexError:
            print("IndexError: list index out of range")
        except ValueError:
            print("ValueError: element not integer")
        except TypeError:
            print("TypeError: cannot print list")
    print("\n")
    return (n)
