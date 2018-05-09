"""
Good morning. Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

Upgrade to premium and get in-depth solutions to every problem.

If you liked this problem, feel free to forward it along! As always, shoot us an email if there's anything we can help with!
"""

def count_decoding(digits, position):
    if position == 0 or position == 1:
        return 1
    count = 0
    if int(digits[position-1]) > 0:
        count += int(count_decoding(digits, position-1))
    if int(digits[position-2]) == 1 or int(digits[position-2]) == 2 and int(digits[position-1]) < 7:
        count += int(count_decoding(digits, position-2))
    return count
digits = str(111)

assert count_decoding(digits, len(digits)) == 3

"""
step through:
                                         count_decoding(111, 3)
                                                  ^
                           count_decoding(111, 2) + count_decoding(111, 1)
                                    ^
             count_decoding(111, 1) + count_decoding(111, 0)

step through:
                                         count_decoding(101, 3)
                                                  ^
                           count_decoding(101, 2) + 0
                                    ^
                                  0 + count_decoding(101, 0)

"""
