#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 0) or (idx >= len(my_list)):
        return None
    else:
        return my_list[idx]
print(element_at([23,4,5,6,7],-5))