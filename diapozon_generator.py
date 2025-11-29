import random

def diap_random(start, end, count):
    for i in range(count):
        yield random.randint(start, end)

start = int(input("Введите нижнюю границу диапозона: "))
end = int(input("Введите верхнюю границу диапозона: "))
count = int(input("Введите количество чисел: "))

print(list(diap_random(start, end, count)))