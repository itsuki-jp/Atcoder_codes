n, m, x = map(int, input().split())
c = []
a = []
ans = float("inf")
for _ in range(n):
    ca = list(map(int, input().split()))
    c.append(ca[0])
    a.append(ca[1:])
for i in range(1 << n):
    temp = [0] * m
    mon = 0
    for j in range(n):
        if (i >> j) & 1:
            mon += c[j]
            for k in range(m):
                temp[k] += a[j][k]
    if sum([_ >= x for _ in temp]) == m:
        ans = min(ans, mon)
print(ans if ans != float("inf") else -1)
