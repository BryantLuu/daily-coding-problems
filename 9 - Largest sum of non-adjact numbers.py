"""
Good morning. Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

Upgrade to premium and get in-depth solutions to every problem.

If you liked this problem, feel free to forward it along! As always, shoot us an email if there's anything we can help with!
"""

def largest_sum_of_non_adjacent_numbers(arr):
    left_index = 0
    left_num = arr[left_index]
    right_index = 2
    right_num = arr[right_index]
    while right_index < len(arr) - 1:
        right_index += 1
        if arr[right_index] > right_num:
            right_num = arr[right_index]
            while left_index < right_index - 2:
                left_index += 1
                if arr[left_index] > left_num:
                    left_num = arr[left_index]
    return left_num + right_num

assert largest_sum_of_non_adjacent_numbers([2, 4, 6, 8]) == 12
assert largest_sum_of_non_adjacent_numbers([5, 1, 1, 5]) == 10
