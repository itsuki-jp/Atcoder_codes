# warshall_floyd法
def warshall_floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    prev[i][j] = prev[k][j]


# n:頂点数　m:辺の数
n, m = map(int, input().split())

# 隣接行列の定義、初期化
# ①コスト(存在しないときはinf)
inf = float("inf")
d = [[inf for _ in range(n + 1)] for _ in range(n + 1)]

# ②自分自身へのコストは０
for i in range(n):
    d[i][i] = 0

# コスト入力（何もないときは１，問題によっては入力時に指定される）
for i in range(m):
    a, b, c = map(int, input().split())
    d[a - 1][b - 1] = c
    d[b - 1][a - 1] = c
prev = [[_ for __ in range(n + 1)] for _ in range(n + 1)]
warshall_floyd()
ans = set()
for start in range(n - 1):
    for goal in range(start + 1, n):
        cur = goal
        while cur != start:
            ans.add((max(cur, prev[start][cur]), min(cur, prev[start][cur])))
            cur = prev[start][cur]
print(m - len(ans))
