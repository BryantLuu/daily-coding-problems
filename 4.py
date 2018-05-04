"""
Good morning. Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

Upgrade to premium and get in-depth solutions to every problem.

If you liked this problem, feel free to forward it along! As always, shoot us an email if there's anything we can help with!
"""

def find_smallest_missing_positive_integer(arr):
    if arr[0] != 1:
        smallest_missing_integer = 1
    else:
        smallest_missing_integer = 2

    for index, value in enumerate(arr):
        if index == 0:
            continue
        if index > 0:
            current_index = index - 1
            current_value = value
            while current_index >= 0 and current_value < arr[current_index]:
                temp_value = current_value
                arr[current_index+1] = arr[current_index]
                arr[current_index] = temp_value
                current_index = current_index - 1
            current_index = current_index+1
            walk_up_index = current_index+1
            while walk_up_index < index and current_value == smallest_missing_integer:
                if arr[walk_up_index] - arr[current_index] > 1:
                    smallest_missing_integer = arr[current_index]+1
                walk_up_index = walk_up_index + 1
                current_index = current_index + 1
    return smallest_missing_integer
