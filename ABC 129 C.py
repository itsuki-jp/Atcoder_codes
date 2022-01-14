n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]

dp = [0] * 10 ** 5 + 10


def chmax( a, b ):
    if a < b:
        return b
    else:
        return a


for i in range(1, n):
    if i == a[0]:
        a.popleft()
        continue
    dp[i] = chmax(dp[i],dp[i-1] )
    if i > 1:
        dp[i] = 1

