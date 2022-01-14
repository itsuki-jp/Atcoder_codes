import sys


def solve( now ):
    global ans
    if visited[now]:
        return
    else:
        visited[now] = 1
        ans += t[now]
    for nxt in a_lst[now]:
        if not visited[nxt]:
            solve(nxt)


sys.setrecursionlimit(10 ** 8)
n = int(input())
a_lst = [[]]
t = [[]]
visited = [0 for _ in range(n + 1)]
for _ in range(n):
    tka = list(map(int, input().split()))
    tt = tka[0]
    t.append(tt)
    kt = tka[1]
    if kt != 0:
        at = tka[2:]
        a_lst.append(at)
    else:
        a_lst.append([])
goal = a_lst[-1]
if len(goal) == 0:
    print(t[-1])
    exit()
ans = 0
for i in goal:
    solve(n)
print(ans)
