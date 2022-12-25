#!
from functools import reduce
print(reduce(lambda x, y: x*y, [x for x in range(1, int(input())+1)]))
#fibonacci
from sys import getsizeof


def fib(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b

print(list(fib(100)))

