n, x, y = map(lambda _: int(_) - 1, input().split())
n += 1
dist = [0] * n
for a in range(n):
    for b in range(a + 1, n):
        d = min(b - a, abs(abs(a - x) + abs(b - y)) + 1)
        dist[d] += 1
print(*dist[1:], sep="\n")
