N, M = map(int, input().split())
graph = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append(B)
    graph[B].append(A)

que = [0]
dist = [None] * N
cnt = [0] * N
dist[0] = 0
cnt[0] = 1
mod = 10**9 + 7
for v in que:
    for vv in graph[v]:
        if dist[vv] is None:
            dist[vv] = dist[v] + 1
            que.append(vv)
            cnt[vv] = cnt[v]
        elif dist[vv] == dist[v] + 1:
            cnt[vv] += cnt[v]
            cnt[vv] %= mod

print(cnt[N - 1])
