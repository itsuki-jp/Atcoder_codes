import heapq


def dijkstra( start ):
    inf = float("inf")
    hq = []
    heapq.heapify(hq)
    dist = [inf] * len(edges)
    ways = [[] for _ in range(n + 1)]
    heapq.heappush(hq, (0, start, ["0"]))
    dist[start] = 0
    while hq:
        min_cost, now, way = heapq.heappop(hq)
        if min_cost > dist[now]:
            continue
        for cost, nxt in edges[now]:
            if dist[nxt] > dist[now] + cost:
                dist[nxt] = dist[now] + cost
                ways[nxt] = way + [str(nxt)]
                heapq.heappush(hq, (dist[nxt], nxt, way + [str(nxt)]))
    return dist, ways


n, m = map(int, input().split())  # 頂点,道
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())  # edge,edge,weight
    edges[a].append([c, b])
q, k = map(int, input().split())  # q-> num of query, k -> start pos

dist, ways = dijkstra(k)
print(dist)
print(*ways, sep="\n")
