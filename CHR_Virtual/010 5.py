from collections import deque
from itertools import permutations

n = int(input())
s = input()
d = {}
for c in ["A", "B", "C"]:
    for i in range(3):
        d[(c, i)] = deque()
for i in range(3 * n):
    d[(s[i], i // n)].append(i)
ans = [-1] * (3 * n)
cur = 1
for i, j, k in permutations([0, 1, 2]):
    while len(d[("A", i)]) > 0 and len(d[("B", j)]) > 0 and len(d[("C", k)]) > 0:
        ans[d[("A", i)].pop()] = cur
        ans[d[("B", j)].pop()] = cur
        ans[d[("C", k)].pop()] = cur
    cur += 1
print(*ans, sep="")
