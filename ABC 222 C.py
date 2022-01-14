n, m = map(int, input().split())
a = [input() for _ in range(2 * n)]
ans = [[0, -i] for i in range(2 * n)]
for mi in range(m):
    for k in range(n):
        p1, p2 = a[-ans[2 * k][1]][mi], a[-ans[2 * k + 1][1]][mi]
        if p1 == "G":
            p1 = 0
        elif p1 == "C":
            p1 = 1
        elif p1 == "P":
            p1 = 2
        if p2 == "G":
            p2 = 0
        elif p2 == "C":
            p2 = 1
        elif p2 == "P":
            p2 = 2
        win_lose = (p1 - p2 + 3) % 3
        if win_lose == 0:
            continue
        elif win_lose == 1:
            ans[2 * k + 1][0] += 1
        else:
            ans[2 * k][0] += 1
    ans = sorted(ans,reverse=True)
for i in ans:
    print(-i[1] + 1)
