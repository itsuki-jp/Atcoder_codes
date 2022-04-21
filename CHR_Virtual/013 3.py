n, m, K = map(int, input().split())
dp = [[0] * (K + 10) for _ in range(n + 10)]
mod = 998244353
dp[0][0] = 1
for i in range(n):
    for j in range(K):
        for k in range(1, m + 1):
            if j + k <= K:
                dp[i + 1][j + k] += dp[i][j] % mod
print(sum(dp[n]) % mod)
