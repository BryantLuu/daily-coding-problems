"""

Good morning. Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

Upgrade to premium and get in-depth solutions to every problem.

If you liked this problem, feel free to forward it along! As always, shoot us an email if there's anything we can help with!
"""

import time

def job_scheduler(f, milliseconds):
    seconds = milliseconds/1000
    time.sleep(seconds)
    f()
