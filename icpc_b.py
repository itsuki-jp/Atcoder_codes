inf = float("inf")
while True:
    solved = False
    w, h = map(int, input().split())
    if w == h == 0:
        exit()
    k = w + h - 1
    top = [0] + [inf] * (w - 1)
    side = [inf] * h
    xyn = sorted([list(map(int, input().split())) for _ in range(k)])
    later = []
    for x, y, n in xyn:
        x -= 1
        y -= 1
        if x == 0:
            side[y] = n
        else:
            if top[x] == side[y] == inf:
                later.append((x, y, n))
            elif side[y] != inf and top[x] == inf:
                top[x] = n - side[y]
            elif side[y] == inf and top[x] != inf:
                side[y] = n - top[x]
            elif side[y] != inf and top[x] != inf and side[y] + top[x] != n:
                print("NO")
                solved = True
                break
    if solved:
        continue
    for i in range(10000):
        temp = later[::1]
        later = []
        if len(temp) == 0:
            break
        for x, y, n in temp:
            if top[x] == side[y] == inf:
                later.append((x, y, n))
            elif side[y] != inf and top[x] == inf:
                top[x] = n - side[y]
            elif side[y] == inf and top[x] != inf:
                side[y] = n - top[x]
            elif side[y] != inf and top[x] != inf and side[y] + top[x] != n:
                print("NO")
                solved = True
                break
    if solved:
        continue
    if sum([1 for i in top if i != inf]) + sum([1 for i in side if i != inf]) == w + h:
        print("YES")
    else:
        print("NO")
