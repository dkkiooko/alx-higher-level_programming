#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if (idx < 0) or (idx >= len(my_list)):
        return my_list
    else:
        del my_list[idx]
        return my_list
j = delete_at([23,4,5,6,6], idx=2)
print(j)