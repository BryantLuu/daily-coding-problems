"""
Good morning. Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

Upgrade to premium and get in-depth solutions to every problem.

If you liked this problem, feel free to forward it along! As always, shoot us an email if there's anything we can help with!
"""

def generator_function():
    for i in range(10):
        yield i

random_select_if_known_size(stream, size):
    count = 1
    random_int = random.randint(1, size)
    for item in stream:
        if count == random_int:
            return item
        count += 1

def random_select_if_unknown_size(stream):
    count = 1
    selected_item = None
    for item in stream:
        random_int = random.randint(1, count)
        # Initial value and then pick every value in the stream with a 1/n chance
        if selected_item == None or random_int != count:
            selected_item = item
    return selected_item

random_select_if_unknown_size(generator_function())
