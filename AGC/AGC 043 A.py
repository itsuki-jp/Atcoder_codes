h, w = map(int, input().split())
board = [list(input()) for _ in range(h)]
inf = float("inf")
lst = [[inf for _ in range(w + 1)] for _ in range(h + 1)]
for _ in range(w + 1):
    lst[0][_] = 0
for _ in range(h + 1):
    lst[_][0] = 0
lst[1][1] = 1 if board[0][0] == "#" else 0
for y in range(h):
    for x in range(w):
        if board[y][x] == ".":
            if x != 0:
                lst[y + 1][x + 1] = lst[y + 1][x]
            if y != 0:
                lst[y + 1][x + 1] = min(lst[y + 1][x + 1], lst[y][x + 1])
        else:
            if x != 0:
                lst[y + 1][x + 1] = lst[y + 1][x] + 1 if board[y][x - 1] == "." else lst[y + 1][x]
            if y != 0:
                lst[y + 1][x + 1] = min(lst[y + 1][x + 1],
                                        lst[y][x + 1] + 1 if board[y - 1][x] == "." else lst[y][x + 1])
print(lst[h][w])
