from collections import deque

h, w = [int(i) - 1 for i in input().split()]
ans = 0
maze = []
for i in range(h + 1):
    s = list(input())
    maze.append(s)
    ans += s.count(".")

pos = deque([[0, 0, 0]])

while pos:
    y, x, b = pos.popleft()
    if y == h and x == w:
        print(ans - b - 1)
        exit()
    for ny, nx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0 <= y + ny <= h and 0 <= x + nx <= w and maze[y + ny][x + nx] == ".":
            pos.append([y + ny, x + nx, b + 1])
            maze[y + ny][x + nx] = "#"
print(-1)
