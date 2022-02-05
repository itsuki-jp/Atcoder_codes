from collections import deque
import heapq

n, m = map(int, input().split())
h = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

inf = -1 * float("ing")
hill = [inf for _ in range(n)]
hill[0] = 0
d = deque()
d.append((0, 0))
