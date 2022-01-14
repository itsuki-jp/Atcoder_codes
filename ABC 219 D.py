n = int(input())
x, y = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

INF = 10 ** 18
num = 301
dp = [[[INF] * (y + 1) for _ in range(x + 1)] for _ in range(n + 1)]
# dp[i][j][k] := i番目までの商品でたこ焼きの合計がj上, たい焼きがk以上となる最小の弁当の個数
for i in range(n + 1):
    dp[i][0][0] = 0

for i in range(n):  # i + 1番目のお弁当を使うかどうか
    xi, yi = ab[i]
    for j in range(x + 1):
        nx = min(x, j + xi)  # たこ焼きの数がxより大きい場合は、考えなくていい -> 考えると、数が大きくなり大変になる
        for k in range(y + 1):
            ny = min(k + yi, y)
            dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])  # i + 1番目のお弁当を買わない
            dp[i + 1][nx][ny] = min(dp[i + 1][nx][ny], dp[i][j][k] + 1)  # i + 1番目のお弁当を買う
ans = -1
if dp[n][x][y] != INF:
    ans = dp[n][x][y]
print(ans)
