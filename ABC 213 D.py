import sys
sys.setrecursionlimit(300000)


def solve( now, pre ):
    ans_lst.append(now)
    for i in graph[now]:
        if i != pre:
            solve(i, now)
            ans_lst.append(now)


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n + 1):
    graph[i].sort()

ans_lst = []
solve(1,-1)
print(*ans_lst)
