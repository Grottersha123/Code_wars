from functools import reduce
def grow(arr):
    return reduce(lambda x, y: x * y, arr)

from operator import muldef grow(arr):
    return reduce(mul, arr)
