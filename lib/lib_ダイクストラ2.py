from heapq import heappop, heappush


def dijkstra( graph, start ):
    n = len(graph)
    dist = [-1] * n
    hq = []
    heappush(hq, (0, start))
    while hq:
        min_cost, now = heappop(hq)
        if dist[now] != -1:
            continue
        dist[now] = min_cost
        for nxt, cost in graph[now]:
            if dist[nxt] != -1:
                continue
            heappush(hq, (min_cost + cost, nxt))
    return dist


def main():
    n, m, x, y = map(int, input().split())
    x -= 1
    y -= 1

    graph = [[] for _ in range(n)]
    for i in range(m):
        s, t, tm = map(int, input().split())
        s -= 1
        t -= 1
        graph[s].append([t, tm])
        graph[t].append([s, tm])

    dist = dijkstra(graph, x)
    print(dist[y])


if __name__ == '__main__':
    main()
