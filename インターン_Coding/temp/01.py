import sys
import numba


def test():
    lines = []
    with open("input01.txt") as f:
        for s_line in f:
            lines.append(s_line.rstrip('\r\n'))
    return lines


def real():
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    return lines


def main( lines ):
    h, a, b = [int(_) for _ in lines[0].split(" ")]
    if a < b and h > a:
        print("NO")
        exit()
    print("YES")
    if h <= a:
        print(1)
    else:
        h -= a
        if h % (a - b) == 0:
            print(h // (a - b) + 1)
        else:
            print(h // (a - b) + 2)


if __name__ == '__main__':
    main(real())
