n, k = map(int, input().split())
s = [int(input()) for _ in range(n)]
if 0 in s:
    exit(print(n))
ans = 0
mul = 1
r = 0
for l in range(n):
    while r < n and s[r] * mul <= k:
        mul *= s[r]
        r += 1
    ans = max(ans, r - l)
    if l == r:
        r += 1
    else:
        mul //= s[l]
print(ans)