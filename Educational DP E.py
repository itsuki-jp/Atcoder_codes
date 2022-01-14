N, W = map(int, input().split())
wv = []
for _ in range(N):
    wvt = list(map(int, input().split()))
    wv.append(wvt)
mv = 10 ** 5 + 1
dp = [[float("inf")] * mv for _ in range(N + 1)]
dp[0][0] = 0
for i in range(1, N + 1):
    wi, vi = wv[i - 1]
    for j in range(mv):
        if j - vi >= 0:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - vi] + wi)
        else:
            dp[i][j] = dp[i - 1][j]

for j in range(mv-1, -1, -1):
    if 0 <= dp[N][j] <= W:
        print(j)
        break
