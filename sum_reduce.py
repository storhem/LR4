import functools
import operator

print(functools.reduce(operator.add, [1, 2, 3]))