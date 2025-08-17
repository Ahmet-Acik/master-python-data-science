"""
functional_tools.py
-------------------
Lambda, map, filter, reduce, zip for functional programming.
"""
from functools import reduce

def functional_examples():
    nums = [1, 2, 3, 4]
    squares = list(map(lambda x: x**2, nums))
    evens = list(filter(lambda x: x % 2 == 0, nums))
    product = reduce(lambda x, y: x * y, nums)
    pairs = list(zip(nums, squares))
    return squares, evens, product, pairs
