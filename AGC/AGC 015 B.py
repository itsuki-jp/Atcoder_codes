s = input()
n = len(s)
ans = 0
for i in range(n):
    pos = i + 1
    if s[i] == "U":
        ans += (n - pos) # 上の階には一発
        ans += (pos - 1) * 2 # 下の階には上がって下がる
    else:
        ans += (n - pos) * 2
        ans += (pos - 1)
print(ans)