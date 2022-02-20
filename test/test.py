from heapq import heappop, heappush

INF = 1 << 62 - 1


def main():
    def dijkstra(G, start):
        N = len(G)
        dist = [INF] * N
        dist[start] = -H[0]
        pq = [(-H[0], start)]
        while pq:
            cost, u = heappop(pq)
            if dist[u] < cost:
                continue
            for v, d in G[u]:
                new_cost = cost + d
                if dist[v] > new_cost:
                    dist[v] = new_cost
                    heappush(pq, (new_cost, v))
        return dist

    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        G[a].append((b, max(0, H[b] - H[a])))
        G[b].append((a, max(0, H[a] - H[b])))
    dist = dijkstra(G, 0)
    ans = max(-dist[i] - H[i] for i in range(N))
    print(ans)