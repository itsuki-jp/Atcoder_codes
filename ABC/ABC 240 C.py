n, x = map(int, input().split())
a = []
b = []
for _ in range(n):
    at, bt = map(int, input().split())
    a.append(at)
    b.append(bt)
dp = [[0 for _ in range(x + 100)] for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(x + 1):
        if dp[i][j] == 1:
            if j + a[i] <= x:
                dp[i + 1][j + a[i]] = 1
            if j + b[i] <= x:
                dp[i + 1][j + b[i]] = 1
if dp[n][x] == 1:
    print("Yes")
else:
    print("No")
