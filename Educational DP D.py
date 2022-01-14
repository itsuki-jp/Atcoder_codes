N, W = map(int, input().split())
w = []
v = []
for _ in range(N):
    tw, tv = map(int, input().split())
    w.append(tw)
    v.append(tv)
dp = [[0] * (W + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    weight = w[i - 1]
    value = v[i - 1]
    for j in range(1, W + 1):
        if weight > j:
            dp[i][j] = dp[i-1][j]
            continue
        dp[i][j] = max(dp[i-1][j - weight] + value, dp[i - 1][j])
print(dp[N][W])
