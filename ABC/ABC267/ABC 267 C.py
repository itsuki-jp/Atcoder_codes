n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
lst = [0]
for i in range(n):
    lst.append(lst[-1] + a[i] * (i + 1))
acc = sum(a[:m + 1])
ans = -float("inf")
now = lst[m]
for i in range(n - m):
    ans = max(now, ans)
    acc += a[m + i + 1] * (i + 1)
    now = lst[i + m + 1] - acc
print(ans)
