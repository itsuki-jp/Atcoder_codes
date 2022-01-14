from collections import deque


def bfs():
    d = deque()
    d.append((0, 0, [0]))
    while d:
        now, pre, res = d.popleft()
        if now == n:
            return res + [str(now)]
        for nxt, nc in graph[now]:
            if visited[nxt]:
                continue
            d.append((nxt, now, res + [str(nxt)]))


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
graph = [sorted(i) for i in graph]
print(bfs()[:-1])
