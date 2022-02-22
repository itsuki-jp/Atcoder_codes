import heapq
from math import ceil

INF = 1 << 100


def dijkstra( edges, start ):
    hq = []
    heapq.heapify(hq)
    dist = [INF] * len(edges)
    heapq.heappush(hq, (0, start))
    dist[start] = 0
    while hq:
        min_cost, now = heapq.heappop(hq)
        if min_cost > dist[now]:
            continue
        for cost, nxt, k in edges[now]:
            n_c = ceil(min_cost / k) * k + cost
            if dist[nxt] > n_c:
                dist[nxt] = n_c
                heapq.heappush(hq, (n_c, nxt))
    return dist


def main():
    n, m, x, y = map(int, input().split())
    x -= 1
    y -= 1

    graph = [[] for _ in range(n)]
    for i in range(m):
        a, b, t, k = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append([t, b, k])
        graph[b].append([t, a, k])

    dist = dijkstra(graph, x)
    print(dist[y] if dist[y] != INF else -1)


if __name__ == '__main__':
    main()
