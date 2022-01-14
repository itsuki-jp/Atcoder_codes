from operator import mul
from functools import reduce


def cmb( n, r ):
    r = min(n - r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


p = int(input()) / 100
ans = 0

for i in range(4, 8):
    num = cmb(7, i)
    temp = (p ** i) * ((1 - p) ** (7 - i)) * num
    ans += temp
print(ans * 100)
