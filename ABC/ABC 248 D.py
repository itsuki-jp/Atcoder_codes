from bisect import *

n = int(input())
a = list(map(int, input().split()))
q = int(input())
lst = [[] for _ in range(10 ** 6)]
for _ in range(n):
    lst[a[_]].append(_ + 1)
for _ in range(q):
    l, r, x = map(int, input().split())
    left = bisect_left(lst[x], l)
    right = bisect_right(lst[x], r)
    print(right - left)
