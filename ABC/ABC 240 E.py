from sys import setrecursionlimit


def solve( pos ):
    global cnt
    if visited[pos]:
        return ans[pos]
    visited[pos] = True
    if pos != 0 and len(graph[pos]) == 1:
        ans[pos] = [cnt, cnt]
        cnt += 1
        return ans[pos]
    big, small = -1, 10 ** 10
    for nxt in graph[pos]:
        if not visited[nxt]:
            temp = solve(nxt)
            big = max(big, temp[1])
            small = min(small, temp[0])
    ans[pos] = [small, big]
    return ans[pos]


setrecursionlimit(10 ** 6)
n = int(input())
ans = [[] for _ in range(n)]
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)
visited = [False for _ in range(n)]
cnt = 1
solve(0)
ans[0] = [1, cnt - 1]
for _ in ans:
    print(*_, sep=" ")
