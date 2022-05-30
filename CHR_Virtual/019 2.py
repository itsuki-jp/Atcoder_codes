n, m = map(int, input().split())
a = [input() for _ in range(2 * n)]
ppl = [[0, -_] for _ in range(2 * n)]
rpc = ["G", "C", "P"]
for i in range(m):
    for j in range(n):
        p1, p2 = a[-ppl[2 * j][1]][i], a[-ppl[2 * j + 1][1]][i]
        p1 = rpc.index(p1)
        p2 = rpc.index(p2)
        res = (p1 - p2 + 3) % 3
        if res == 0:
            continue
        elif res == 2:
            ppl[2 * j][0] += 1
        else:
            ppl[2 * j + 1][0] += 1
    ppl.sort(reverse=True)
for i in ppl:
    print(-i[1] + 1)
