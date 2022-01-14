def warshall_floyd( d ):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        return d


n, m = map(int, input().split())
d = [[float("inf") for i in range(n)] for i in range(n)]
for i in range(n):
    d[i][i] = 0
for i in range(m):
    a, b, cost = map(int, input().split())
    d[a - 1][b - 1] = cost
    d[b - 1][a - 1] = cost
print(*warshall_floyd(d),sep="\n")




# efjnfjbnfnb
n, m = map(int, input().split())

w = [[0] * n for _ in range(n)]
for i in range(m):
    a, b, cost = map(int, input().split())
    w[a - 1][b - 1] = cost
    w[b - 1][a - 1] = cost


def solve( w ):
    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if i == j:
                val = 0
            elif w[i][j]:
                val = w[i][j]
            else:
                val = float("inf")
            res[i][j] = res[j][i] = val
    for k in range(n):
        for i in range(n):
            for j in range(n):
                res[i][j] = min(res[i][j], res[i][k] + res[k][j])
    return res


lst = solve(w)
print(*lst,sep="\n")
ans = [sum(lst[i]) for i in range(n)]
print(sum(ans))

