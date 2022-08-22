def end():
    print(-1)
    exit()


def out( i, j ):
    print(i + 1, j + 1)
    exit()


h, w = map(int, input().split())
g = [list(input()) for _ in range(h)]
pos = (0, 0)

while True:
    i, j = pos
    if g[i][j] == "A":
        end()
    if g[i][j] == "U":
        if i != 0:
            pos = (i - 1, j)
        else:
            out(i, j)
    elif g[i][j] == "D":
        if i != h - 1:
            pos = (i + 1, j)
        else:
            out(i, j)
    elif g[i][j] == "L":
        if j != 0:
            pos = (i, j - 1)
        else:
            out(i, j)
    else:
        if j != w - 1:
            pos = (i, j + 1)
        else:
            out(i, j)
    g[i][j] = "A"
