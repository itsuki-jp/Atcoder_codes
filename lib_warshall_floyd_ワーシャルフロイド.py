# warshall_floyd法
def warshall_floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])


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
cost = 1
for i in range(m):
    a, b = map(int, input().split())
    d[a][b] = cost
    d[b][a] = cost

warshall_floyd()
