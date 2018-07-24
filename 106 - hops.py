# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Pinterest.
#
# Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.
#
# For example, [2, 0, 1, 0] returns true while [1, 1, 0, 1] returns false.
#
# Upgrade to premium and get in-depth solutions to every problem.
#
# If you liked this problem, feel free to forward it along so they can subscribe here! As always, shoot us an email if there's anything we can help with!

def can_hop(arr):
    hops = 0
    for i in range(len(arr)):
        hops += arr[i]
        if i+1 > hops:
            return False
    return True
