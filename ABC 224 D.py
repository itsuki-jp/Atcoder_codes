# -*- coding: utf-8 -*-
from collections import deque

m = int(input())
graph = [[] for _ in range(9)]
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    graph[u].append(v)
    graph[v].append(u)
p = list(map(int, input().split()))
p_n = [8] * 9
for pp in range(8):
    p_n[p[pp] - 1] = pp
goal = [i for i in range(8)] + [8]
d = deque()
d.append([-1, p_n.index(8), p_n, 0])
total = 0
sets = set()
while d and total < 10 ** 5:
    pre, pos, lst, cnt = d.popleft()
    if lst == goal:
        exit(print(cnt))
    for nx in graph[pos]:
        if nx == pre:
            continue
        nx_lst = lst[:]
        nx_lst[nx], nx_lst[pos] = nx_lst[pos], nx_lst[nx]
        s = "".join([str(ss) for ss in nx_lst])
        if s in sets:
            continue
        sets.add(s)
        d.append([pos, nx, nx_lst, cnt + 1])
        total += 1
print(-1)
