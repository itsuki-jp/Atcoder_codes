from math import gcd
from functools import reduce
def my_gcd(*numbers):
    return reduce(gcd, numbers)
n, X = map(int, input().split())
x = list(map(int, input().split())) + [X]
x = list(sorted(x))
lst = [x[i+1] - x[i] for i in range(n)]
print(my_gcd(*lst))