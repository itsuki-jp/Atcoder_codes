n, q = map(int, input().split())
a = [_ + 1 for _ in range(n)]
d = {_ + 1: _ for _ in range(n)}
for _ in range(q):
    x = int(input())
    pos = d[x]
    if not pos == n - 1:
        d[x], d[a[pos + 1]] = d[a[pos + 1]], d[x]
        a[pos], a[pos + 1] = a[pos + 1], a[pos]
    else:
        d[x], d[a[pos - 1]] = d[a[pos - 1]], d[x]
        a[pos], a[pos - 1] = a[pos - 1], a[pos]
print(*a)
