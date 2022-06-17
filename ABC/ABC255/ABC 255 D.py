# 解説

from itertools import accumulate
from bisect import *

n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
acc = [0] + list(accumulate(a))
ans = [0] * q
j = 0
for _ in range(q):
    x = int(input())
    right = bisect_right(a, x)

    print()
