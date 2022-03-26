# CHR_Virtual_08
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mod = 998244353
dp = [[0 for _ in range(3000 + 10)] for _ in range(n + 1)]
dp[0] = [1 for _ in range(3000 + 10)]
for i in range(n):
    for j in range(1, 3000 + 9):
        if a[i] <= j <= b[i]:
            dp[i + 1][j] = dp[i + 1][j - 1] + dp[i][j]
print(dp[2][:20])
