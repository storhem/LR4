import functools
import operator

inp = list(map(int, input("Введите числа для суммирования через пробел: ").split()))

print(functools.reduce(operator.add, inp))