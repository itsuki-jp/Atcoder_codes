from bisect import *
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
d = defaultdict(list)
for _ in range(n):
    d[a[_]].append(_ + 1)

q = int(input())
for _ in range(q):
    l, r, x = map(int, input().split())
    left = bisect_left(d[x], l, 0, len(d[x]))
    right = bisect_right(d[x], r, 0, len(d[x]))
    print(right - left)
