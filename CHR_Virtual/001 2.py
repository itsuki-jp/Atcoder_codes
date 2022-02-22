from collections import deque

h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
if c[0][0] == "#":
    print(0)
    exit()
d = deque()
d.append((0, 0, 1))
ans = 1
while d:
    x, y, cnt = d.popleft()
    ans = max(ans, cnt)
    if 0 <= x + 1 < w and c[y][x + 1] != "#":
        d.append((x + 1, y, cnt + 1))
        c[y][x + 1] = "#"
    if 0 <= y + 1 < h and c[y + 1][x] != "#":
        d.append((x, y + 1, cnt + 1))
        c[y + 1][x] = "#"
print(ans)
