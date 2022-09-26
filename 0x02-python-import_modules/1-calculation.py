#!/usr/bin/python3
from caluclator_1 import add
from calculator_1 import sub
from calculator_1 import mul
from calculator_1 import div
if __name__ == "__main__":
    a = 10
    b = 5
    print('{:d} + {:d} = {:d}'.format(a, b, add(a=a, b=b)))
    print('{:d} - {:d} = {:d}'.format(a, b, sub(a=a, b=b)))
    print('{:d} * {:d} = {:d}'.format(a, b, mul(a=a, b=b)))
    print('{:d} / {:d} = {:d}'.format(a, b, div(a=a, b=b)))
