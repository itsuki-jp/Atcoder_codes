import sys
import math
from itertools import combinations
from functools import reduce


def test():
    lines = []
    with open("input04.txt") as f:
        for s_line in f:
            lines.append(s_line.rstrip('\r\n'))
    return lines


def real():
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    return lines


def multiple( L, R, num ):
    return R // num - (L - 1) // num


def my_lcm_base( x, y ):
    return (x * y) // math.gcd(x, y)


def my_lcm( *numbers ):
    return reduce(my_lcm_base, numbers, 1)


def main( lines ):
    l, r = map(int, lines[0].split())
    m = int(lines[1])
    n = list(map(int, lines[2].split()))
    ans = r - l + 1
    for i in n:
        ans -= multiple(l, r, i)
    for i in range(2, m + 1):
        for comb in combinations(n, i):
            ans += multiple(l, r, my_lcm(*list(comb)))
    print(ans)


if __name__ == '__main__':
    main(test())
