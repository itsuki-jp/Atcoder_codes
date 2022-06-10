from heapq import *
from collections import defaultdict

q = int(input())
big2sml = []
sml2big = []
d = defaultdict(int)
for _ in range(q):
    Q = input().split()
    if Q[0] == "1":
        x = int(Q[1])
        if d[x] == 0:
            heappush(big2sml, -x)
            heappush(sml2big, x)
        d[x] += 1
    elif Q[0] == "2":
        x, c = map(int, Q[1:])
        d[x] -= min(d[x], c)
    else:
        while True:
            val = heappop(big2sml)
            if d[-val] != 0:
                heappush(big2sml, val)
                res = -val
                break
        while True:
            val = heappop(sml2big)
            if d[val] != 0:
                heappush(sml2big, val)
                print(res - val)
                break
