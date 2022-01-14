from collections import defaultdict
from itertools import accumulate

n = int(input())
v = [[] for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    v[i].append(a)
    v[i].append(a + b)
com = []
for i in v:
    com.extend(i)
com = sorted(set(com))
m = len(com)
d = defaultdict()
for i in range(m):
    d[com[i]] = i
imos = [0 for _ in range(m + 1)]
for i in v:
    imos[d[i[0]]] += 1
    imos[d[i[1]]] -= 1
imos = list(accumulate(imos))
ans = [0 for _ in range(n + 1)]
for i in range(m - 1):
    ans[imos[i]] += com[i + 1] - com[i]
print(*ans[1:])
