from sys import setrecursionlimit


def solve( now, prv=-1 ):
    global cnt
    l[now] = cnt
    for nxt in graph[now]:
        if nxt == prv:
            continue
        solve(nxt, now)
    if (len(graph[now])) == 1 and prv != -1:
        cnt += 1
    r[now] = cnt - 1


setrecursionlimit(10 ** 6)
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    ut, vt = map(int, input().split())
    graph[ut - 1].append(vt - 1)
    graph[vt - 1].append(ut - 1)
cnt = 1
r = [0] * n
l = [0] * n
solve(0)
for _ in range(n):
    print(l[_], r[_])
