from heapq import *

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
h = []
heappush(h, (0, n - 1, 0))
visited = set()

ans = 10 ** 10
while h:
    cost, x, y = heappop(h)
    if (x, y) in visited:
        continue
    visited.add((x, y))
    if x == 0 and y == n - 1:
        print(cost + a[0][-1])
        exit()
    for dx, dy in [(-1, 0), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            heappush(h, (cost + a[ny][nx], nx, ny))
print(ans)
