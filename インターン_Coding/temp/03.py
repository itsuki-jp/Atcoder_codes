import sys
from heapq import *


def test():
    lines = []
    with open("input03.txt") as f:
        for s_line in f:
            lines.append(s_line.rstrip('\r\n'))
    return lines


def real():
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    return lines


def main( lines ):
    n, m, k = map(int, lines[0].split())
    tate = [0 for _ in range(n)]
    yoko = [0 for _ in range(m)]
    c = []
    for i in range(n):
        c_temp = lines[i + 1]
        c.append(list())
        for j in range(m):
            c[-1].append(c_temp[j])
            if c_temp[j] == "B":
                tate[i] = 1
                yoko[j] = 1
    bombed = []
    safe = []
    for y in range(n):
        for x in range(m):
            now = c[y][x]
            if tate[y] or yoko[x]:
                if now != "B":
                    bombed.append(int(now))
            else:
                safe.append(int(now))
    bombed.sort()
    safe.sort(reverse=True)
    ans = sum(safe)
    for i in range(k):
        if len(bombed) == 0 or len(safe) != 0:
            break
        elif bombed[-1] > safe[-1]:
            ans += bombed.pop() - safe.pop()
        else:
            break
    print(ans)


if __name__ == '__main__':
    main(test())
