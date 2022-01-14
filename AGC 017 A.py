n, p = map(int, input().split())
a = list(map(int, input().split()))
lim = 50 * 100 + 1
dp = [[0 for _ in range(lim)] for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(lim):
        dp[i + 1][j] = dp[i][j]
        if j >= a[i]:
            dp[i+1][j] += dp[i][j - a[i]]
ans = 0
for i in range(lim):
    if i % 2 == p and dp[-1][i] != 0:
        ans += dp[-1][i]
print(ans)
