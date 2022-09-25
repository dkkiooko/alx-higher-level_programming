#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = [True if i%2==0 else False for i in my_list ]
    return result
j = divisible_by_2([2,4,5,6,6,7])
print(j)