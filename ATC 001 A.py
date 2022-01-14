h, w = map(int, input().split())
maze = [list(input()) for _ in range(h)]

for y in range(h):  # スタート地点探す
    for x in range(w):
        if maze[y][x] == "s":
            sy, sx = y, x


def dfs(y, x):
    if not 0 <= x < w or not 0 <= y < h or maze[y][x] == "#":  # 迷路外か壁・探索済み
        return False
    if maze[y][x] == "g":  # ゴールに着いた
        print("Yes")
        exit()
    maze[y][x] = "#"
    dfs(y + 1, x)
    dfs(y - 1, x)
    dfs(y, x - 1)
    dfs(y, x + 1)  # 全部探す


dfs(sy, sy)
print("No")
