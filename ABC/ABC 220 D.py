n = int(input())
a = list(map(int, input().split()))
mod = 998244353
dp = [[0 for _ in range(10)] for _ in range(n + 10)]
dp[0][a[0]] = 1
for i in range(1, n):
    for j in range(10):
        if dp[i - 1][j]:
            dp[i][(j * a[i]) % 10] += dp[i - 1][j]
            dp[i][(j + a[i]) % 10] += dp[i - 1][j]
            dp[i][(j * a[i]) % 10] %= mod
            dp[i][(j + a[i]) % 10] %= mod

print(*dp[n - 1], sep="\n")
