"""
Good morning. Here's your coding interview problem for today.

Given a list of numbers, return whether any two sums to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

Upgrade to premium and get in-depth solutions to every problem.

If you liked this problem, feel free to forward it along! As always, shoot us an email if there's anything we can help with!
"""

def sumTo(nums, k):
    already_passed_numbers = set()
    for num in nums:
        if already_passed_numbers:
            if k-num in already_passed_numbers:
                return True
        already_passed_numbers.add(num)
    return False

assert sumTo([10, 15, 3, 7], 17) == True
