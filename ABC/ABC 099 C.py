N = int(input())
num_lst = [1 for _ in range(5)] + [6 ** i for i in range(1, 7)] * 5 + [9 ** i for i in range(1, 8)]* 5
l = len(num_lst)
big = 10 ** 5
dp = [[big for _ in range(N + 10)] for _ in range(l + 10)]
dp[0][0] = 0
for i in range(l):
    for j in range(N + 1):
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        if j >= num_lst[i]:
            dp[i+1][j] = min(dp[i+1][j], dp[i][j - num_lst[i]] + 1)
print(dp[l][N])