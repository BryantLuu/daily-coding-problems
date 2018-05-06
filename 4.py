"""
Good morning. Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

Upgrade to premium and get in-depth solutions to every problem.

If you liked this problem, feel free to forward it along! As always, shoot us an email if there's anything we can help with!
"""

def get_positive_array_portion(arr):
    first_positive_index = None
    i = -1
    for j in range(len(arr)):
        if arr[j] <= 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    for j in range(len(arr)):
        if arr[j] > 0:
            return arr[j:]

def find_smallest_missing_positive_integer(arr):
    arr = get_positive_array_portion(arr)
    for i in range(len(arr)):
        if abs(arr[i]) <= len(arr) and arr[abs(arr[i])-1] > 0:
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
    for i in range(len(arr)):
        if arr[i] > 0:
            return i+1
    return len(arr)+1

assert find_smallest_missing_positive_integer([3, 4, -1, 0, 1]) == 2
assert find_smallest_missing_positive_integer([1, 2, 0]) == 3
assert find_smallest_missing_positive_integer([1, 5, 7]) == 2
