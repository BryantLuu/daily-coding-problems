"""

Good morning. Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

Upgrade to premium and get in-depth solutions to every problem.

If you liked this problem, feel free to forward it along! As always, shoot us an email if there's anything we can help with!
"""

from functools import reduce

def product_of_other_numbers(arr):
    total_product = reduce(lambda x, y: x*y, arr)
    return list(map(lambda x: total_product/x, arr))

assert product_of_other_numbers([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]

def product_of_other_numbers_without_divide(arr):
    return_list = list()
    for counter, value in enumerate(arr):
        copy = list(arr)
        del copy[counter]
        return_list.append(
            reduce(lambda x,y: x*y, copy)
        )
    return return_list

assert (
    product_of_other_numbers_without_divide([1, 2, 3, 4, 5]) ==
    [120, 60, 40, 30, 24]
)
