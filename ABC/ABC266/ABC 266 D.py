n = int(input())

txa = {}
mxT = 0
for _ in range(n):
    t, x, a = map(int, input().split())
    if t not in txa:
        txa[t] = dict()
    txa[t][x] = a
    mxT = max(mxT, t)

dp = [[0 for _ in range(10)] for _ in range(n + 10)]
for i in range(mxT + 1):
    for j in range(6):
        if j == 0:
            if i in txa:
                if 1 in txa[i]:
                    dp[i + 1][1] = max(dp[i][1], dp[i][0] + txa[i][1])
                if 0 in txa[i]:
                    dp[i + 1][0] = max(dp[i][0], dp[i][0] + txa[i][0])
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j + 1], dp[i][j])
        elif j == 5:
            if i in txa:
                if 4 in txa[i]:
                    dp[i + 1][4] = max(dp[i][4], dp[i][5] + txa[i][4])
                if 5 in txa[i]:
                    dp[i + 1][5] = max(dp[i][5], dp[i][5] + txa[i][5])
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - 1], dp[i][j])
        else:
            if i in txa:
                if j - 1 in txa[i]:
                    dp[i + 1][j - 1] = max(dp[i][j - 1], dp[i][j] + txa[i][j - 1])
                if j in txa[i]:
                    dp[i + 1][j] = max(dp[i][j], dp[i][j] + txa[i][j])
                if j + 1 in txa[i]:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i][j] + txa[i][j + 1])
            dp[i + 1][j] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j], dp[i][j - 1])
print(*dp, sep="\n")
