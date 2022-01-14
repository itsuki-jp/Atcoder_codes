h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
lst = ["#" * (2 + w)] * h
for i in range(h):
    a = list(input())
    print(a)
    lst[i][1:w] = a
    print(lst)
print(lst)
lst[dh - 1][dw - 1] = "G"
wall = "#"


def solve(maze, y, x, cnt):
    if maze[y][x] == "G":
        print(cnt)
        exit()
    maze[y][x] = wall
    for (next_y, next_x) in [(y + 1, x), (y, x + 1), (y, x - 1), (y - 1, x)]:
        if maze[next_y][next_x] == wall:
            continue
        route = solve(maze, next_y, next_x, cnt)
        if route:
            return [(y, x)] + route
    print(-1)


solve(lst, ch - 1, cw - 1, 0)
