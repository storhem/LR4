import random

def diap_random(start, end, count):
    for _ in range(count):
        yield random.randint(start, end)