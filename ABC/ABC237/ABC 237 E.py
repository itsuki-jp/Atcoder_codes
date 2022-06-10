import heapq

INF = 10 ** 30


# ----------------------------------------------------------------
# https://qiita.com/Kept1994/items/0b185def44fca1aa64ed#%E3%83%80%E3%82%A4%E3%82%AF%E3%82%B9%E3%83%88%E3%83%A9%E6%B3%95
# Input
#   1. タプル(重み, 行先)の二次元配列(隣接リスト)
#   2. 探索開始ノード(番号)
# Output
#   スタートから各ノードへの最小コスト
# ----------------------------------------------------------------
def dijkstra( edges: "List[List[(cost, to)]]", start_node: int ) -> list:
    hq = []
    heapq.heapify(hq)
    # Set start info
    dist = [INF] * len(edges)
    heapq.heappush(hq, (0, start_node))
    dist[start_node] = 0
    # dijkstra
    while hq:
        # ------------------------------------------- タイミング1
        min_cost, now = heapq.heappop(hq)
        # ------------------------------------------- タイミング2
        if min_cost > dist[now]:
            continue
        for cost, next in edges[now]:
            if dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost
                heapq.heappush(hq, (dist[next], next))
            # --------------------------------------- タイミング3
    return dist


n, m = map(int, input().split())  # 頂点,道
h = list(map(int, input().split()))
edge = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())  # edge,edge,weight
    if a >= b:
        edge[a].append()
        edge[b].append()
q, k = map(int, input().split())  # q-> num of query, k -> start pos
dist = dijkstra(edge, k)
