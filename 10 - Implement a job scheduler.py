import time

def job_scheduler(f, milliseconds):
    seconds = milliseconds/1000
    time.sleep(seconds)
    f()
