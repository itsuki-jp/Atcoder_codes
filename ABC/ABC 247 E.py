n, x, y = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
r = 0
sm, bg = a[0], a[0]
for l in range(n):
    sm = min(a[l], sm)
    bg = max(a[l], bg)

