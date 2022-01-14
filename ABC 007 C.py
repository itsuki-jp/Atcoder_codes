from collections import deque

r, c = map(int, input().split())
sy, sx = [int(s) - 1 for s in input().split()]
gy, gx = [int(s) - 1 for s in input().split()]

maze = [list(input()) for _ in range(r)]

now = deque([[sy, sx, 0]])

while now:
    ny, nx, ans = now.popleft()
    if ny == gy and nx == gx:
        print(ans)
        exit()
    for y, x in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        if maze[ny + y][nx + x] == ".":
            now.append([ny + y, nx + x, ans + 1])
            maze[ny + y][nx + x] = "#"