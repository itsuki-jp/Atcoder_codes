import sys

sys.setrecursionlimit(10 ** 5)


def solve( pos ):
    if visited[pos]:
        return ans[pos]
    visited[pos] = True
    if len(graph[pos]) == 0:
        return a[pos]
    val = small
    for nxt in graph[pos]:
        ans[nxt] = max(solve(nxt), a[nxt])
        val = max(val, ans[nxt])
    ans[pos] = max(val, a[pos])
    return ans[pos]


n, m = map(int, input().split())
a = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y = [int(_) - 1 for _ in input().split()]
    graph[x].append(y)
small = -float("inf")
ans = [small for _ in range(n)]
visited = [False for _ in range(n)]
for i in range(n):
    solve(i)
res = small
for i in range(n):
    res = max(res, ans[i] - a[i])
print(res)
