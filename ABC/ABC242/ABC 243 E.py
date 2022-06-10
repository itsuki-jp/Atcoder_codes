# 解説AC
# warshall_floyd法
def warshall_floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]


# n:頂点数　m:辺の数
n, m = map(int, input().split())

# 隣接行列の定義、初期化
# ①コスト(存在しないときはinf)
inf = float("inf")
d = [[inf for _ in range(n)] for _ in range(n)]

# コスト入力（何もないときは１，問題によっては入力時に指定される）
abc = []
for i in range(m):
    a, b, c = map(int, input().split())
    d[a - 1][b - 1] = c
    d[b - 1][a - 1] = c
    abc.append((a - 1, b - 1, c))
warshall_floyd()
ans = 0
for s_a, s_b, s_c in abc:
    temp = 0
    for i in range(n):
        if d[s_a][i] + d[i][s_b] <= s_c:
            temp = 1
    ans += temp
print(ans)
