from collections import deque

n, x, y = map(int, input().split())
a = list(map(int, input().split()))

A = []
temp = []
for _ in a:
    if y <= _ <= x:
        temp.append(_)
    else:
        A.append(temp)
        temp = []
A.append(temp)
ans = 0
for i in A:
    d = {x: 0, y: 0}
    for l in range(len(i)):
        while d[x] > 0 and d[y] > 0:
