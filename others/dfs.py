def solve( now, cnt ):
    if visited[now]:
        return 0
    if cnt == n - 1:
        return 1
    res = 0
    visited[now] = True
    for nxt in graph[now]:
        res += solve(nxt, cnt + 1)
    visited[now] = False
    return res


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n + 1)
print(solve(1, 0))
