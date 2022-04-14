from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split())) + [10 ** 10]
ans = n * (n + 1) // 2
r = 0
total = 0
for l in range(n):
    while r < n and total + a[r] < k:
        total += a[r]
        r += 1
    ans -= (r - l)
    if r == l:
        r += 1
    else:
        total -= a[l]
print(ans)
