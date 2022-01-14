n = int(input())
ans = 0
xy = [list(map(int, input().split())) for _ in range(n)]
for i in range(n - 1):
    x1, y1 = xy[i]
    for j in range(i + 1, n):
        x2, y2 = xy[j]
        dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        ans = max(ans, dist)
print(ans)
