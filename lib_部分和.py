a = [7, 5, 3, 1, 8]
num = 12
A = sum(a)
dp = [0] * (A + 1)
dp[0] = 1
for i in a:
    for j in range(A, -1, -1):
        if dp[j] != 0:
            dp[j + i] += 1
print(dp[num])
