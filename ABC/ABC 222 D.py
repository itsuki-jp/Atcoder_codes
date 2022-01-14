n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if n == 1:
    exit(print(b[0] - a[0] + 1))
mod = 998244353
mx = 3010
dp = [[0] * mx for _ in range(mx)]
for jj in range(a[0], b[0] + 1):
    dp[0][jj] += 1
for i in range(1, n):
    for j in range(a[i], b[i] + 1):
        dp[i][j] += dp[i - 1][j] +

