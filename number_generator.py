import random
import itertools

def infinity_random():
    for _ in itertools.count():
        yield random.randint(-9999, 9999)

inp = int(input("Введите количество чисел: "))

print(list(itertools.islice(infinity_random(), inp)))