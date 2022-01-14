from functools import reduce
import math


def my_gcd( *numbers ):
    return reduce(math.gcd, numbers)


a, b, c = map(int, input().split())

r = my_gcd(a, b, c)
print(a // r + b // r + c // r - 3)
