from sys import setrecursionlimit


def solve( idx ):
    visited[idx] = 1
    tf = False
    res = lst[idx]
    for nxt in graph[idx]:
        if visited[nxt]:
            continue
        res += solve(nxt)
        tf = True
    if not tf:
        return res
    res.sort(reverse=True)
    lst[idx] = res[:min(len(res), 20)]
    return lst[idx]


setrecursionlimit(10 ** 7)
n, q = map(int, input().split())
x = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
length = [(_, len(graph[_])) for _ in range(n)]
lst = [[x[_]] for _ in range(n)]
visited = [0 for _ in range(n)]

solve(0)
for _ in range(n):
    lst[_] = lst[_][::-1]
for _ in range(q):
    v, k = map(int, input().split())
    v -= 1
    print(lst[v][k - 1])
