import random
import itertools

def infinity_random():
    for _ in itertools.count():
        yield random.randint(-9999, 9999)