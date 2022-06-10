h, w = map(int, input().split())
r, c = map(int, input().split())
ans = 0
for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    x += r
    y += c
    if not 0 < x <= h or not 0 < y <= w:
        continue
    if abs(x - r) + abs(y - c) == 1:
        ans += 1
print(ans)
