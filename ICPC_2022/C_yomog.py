import sys


def group_n( n, m ):
    div = m - 1
    # if div == 0:
    if div <= 1:
        # n を単置き
        return (n, 1, 0, 0)
    if n <= div:
        m3 = n
        m4 = div - m3
        return (1, m3, 0, m4)
    m3 = n - (m - 2)
    m4 = div - m3
    rest = n - m3
    # assert m3 >= 0 and m4 >= 0
    return (1, m3, rest, m4)


def group_m( n, m ):
    mn = m // (n + 1)
    m2 = m - mn * (n + 1)
    m1 = n + 1 - m2
    # print("n:", n, "m:", m, file=sys.stderr)
    # print(f"{mn} が {m1} 個", file=sys.stderr)
    # print(f"{mn + 1} が {m2} 個", file=sys.stderr)
    # assert m1 >= 0 and m2 >= 0
    return (mn, m1, mn + 1, m2)


while True:
    n, m = map(int, input().split())
    if not n and not m:
        break
    if m == 0:
        print(n ** 2)
        continue
    if n == 0:
        print(-(m ** 2))
        continue
    one, m3, rest, m4 = group_n(n, m)
    print("(add) one:", one, "m3:", m3, "rest:", rest, "m4:", m4, file=sys.stderr)
    mn, m1, mn1, m2 = group_m(n, m)
    add = one ** 2 * m3 + rest ** 2 * m4
    sub = mn ** 2 * m1 + mn1 ** 2 * m2
    print("add:", add, "sub:", sub, file=sys.stderr)
    ans = add - sub
    print(ans)
