n, m, K = map(int, input().split())
mod = 998244353
dp = [[0] * (K + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(K + 1):
        for k in range(1, m + 1):
            if j + k <= K:
                dp[i + 1][j + k] += dp[i][j] % mod
ans = sum(dp[-1]) % mod
print(ans)
