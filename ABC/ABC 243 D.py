# 解説AC
def solve1():
    n, x = map(int, input().split())
    s = input()
    b = list(bin(x)[2:])
    for i in s:
        if i == "L":
            b.append("0")
        elif i == "R":
            b.append("1")
        else:
            b.pop()
    print(int("".join(b), 2))


def solve2():
    n, x = map(int, input().split())
    s = input()
    lst = []
    for i in s:
        if len(lst) > 0 and lst[-1] in ("L", "R") and i == "U":
            lst.pop()
            continue
        else:
            lst.append(i)
    for i in lst:
        if i == "U":
            x //= 2
        elif i == "L":
            x *= 2
        else:
            x = x * 2 + 1
    print(x)


solve2()
