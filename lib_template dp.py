n = int(input())
h = [int(i) for i in input().split()]


# dpの最小値を変更する関数
def chmin(a, b):
    if a > b:
        return b
    else:
        return a


# 無限大の値
f_inf = float('inf')
# DP テーブルを初期化　(最小化問題なので INF に初期化)
dp = [f_inf] * (10 ** 5 + 10)
# 初期条件
dp[0] = 0
# 足場 i-1 から足場 i へ移動する。コストは|h[i]−h[i-1]|
# 足場 i-2 から足場 i へと移動する コストは |h[i]−h[i-2]|
for i in range(1, n):
    dp[i] = chmin(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]))
    # 一番目の足場では一つ前しか存在しない
    if i > 1:
        dp[i] = chmin(dp[i], dp[i - 2] + abs(h[i] - h[i - 2]))
print(dp[n - 1])