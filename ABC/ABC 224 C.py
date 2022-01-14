# -*- coding: utf-8 -*-
from operator import mul
from functools import reduce


def cmb( n, r ):
    r = min(n - r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
ans = cmb(n, 3)
for i in range(n - 2):
    x1, y1 = xy[i]
    for j in range(i + 1, n - 1):
        x2, y2 = xy[j]
        for k in range(j + 1, n):
            x3, y3 = xy[k]
            dx2 = x3 - x2
            dx1 = x2 - x1
            dy2 = y3 - y2
            dy1 = y2 - y1
            if dx2 * dy1 == dx1 * dy2:
                ans -= 1
print(ans)