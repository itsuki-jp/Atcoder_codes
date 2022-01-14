def dfs( now, pre ):
    if now == n:
        return str(n)
    visited[now] = 1
    for np, nc in graph[now]:
        if np == pre or visited[np]:
            continue
        res = dfs(np, now)
        if res:
            return str(np) + res


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
graph = [sorted(i) for i in graph]
print(dfs(0, -1)[:-1])
