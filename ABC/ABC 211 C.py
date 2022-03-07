s = input()
mod = 10 ** 9 + 7
chokudai = "chokudai"  # length = 8
dp = [0 for _ in range(8)]
for i in range(len(s)):
    if s[i] not in chokudai:
        continue
    pos = chokudai.index(s[i])
    if pos == 0:
        dp[0] += 1
    else:
        dp[pos] = dp[pos] + dp[pos - 1]
print(dp[-1] % mod)
