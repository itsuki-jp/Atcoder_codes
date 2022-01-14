from math import gcd
from functools import reduce

n, k = map(int, input().split())
a = list(map(int, input().split()))
g = reduce(gcd, a)
if k <= max(a) and k % g == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")