n, s = map(int, input().split())
a = list(map(int, input().split()))
dp = [[0 for _ in range(s + 1)] for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(s + 1):
        dp[i + 1][j] = dp[i][j]
        if 0 <= j - a[i] < s + 1 and dp[i][j - a[i]]:
            dp[i + 1][j] += dp[i][j - a[i]]
print("Yes" if dp[n][s] else "No")
