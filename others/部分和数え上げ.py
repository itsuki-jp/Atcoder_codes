a = [7, 5]
num = 2
dp = [float("inf")] * (num + 1)
dp[0] = 0
for i in a:
    for j in range(num, -1, -1):
        if i + j <= num:
            dp[j + i] = min(dp[j] + 1, dp[i + j])
print(dp[num] if dp[num] != float("inf") else -1)
