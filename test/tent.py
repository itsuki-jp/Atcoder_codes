n, k, x = map(int, input().split())
a = list(map(int, input().split()))
t_k = 0
for i in range(n):
    t_k += a[i] // x
    a[i] %= x
ans = sum(a)
if t_k >= k:
    ans += (t_k - k) * x
else:
    a.sort()
    for j in range(min((k - t_k), n)):
        ans -= a[-j - 1]
print(ans)
