n, c, k = map(int, input().split())
t = [int(input()) for _ in range(n)]
t.sort()
ans = 1
num = 1
border = [t[0], t[0] + k]
for i in range(1, n):
    if num < c:
        if border[0] <= t[i] <= border[1]:
            num += 1
        else:
            ans += 1
            num = 1
            border = [t[i], t[i] + k]
    else:
        ans += 1
        num = 1
        border = [t[i], t[i] + k]
print(ans)
