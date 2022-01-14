import math
from functools import reduce

def my_gcd(*numbers):
    return reduce(math.gcd, numbers)

print(my_gcd(12,15*6,18))