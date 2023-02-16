import sys


def test():
    lines = []
    with open("input02.txt") as f:
        for s_line in f:
            lines.append(s_line.rstrip('\r\n'))
    return lines


def real():
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    return lines


def main( lines ):
    n, k = map(int, lines[0].split())
    s = lines[1]
    s += "." if s[0] == "S" else "S"
    counter = [0] * 3
    count = 0
    pre = "." if s[0] == "S" else "S"
    for i in range(n + 1):
        if pre == ".":
            if s[i] == ".":
                continue
            else:
                count = 1
        else:
            if s[i] == ".":
                if count == 3:
                    counter[0] += 1
                elif count != 0:
                    counter[count % 3] += 1
                count = 0
            else:
                if count == 3:
                    counter[0] += 1
                    count = 0
                count += 1
        pre = s[i]
    ans = s[:-1].count(".")

    if counter[0] <= k:
        ans += counter[0] * 3
        k -= counter[0]
    else:
        ans += k * 3
        k = 0

    if counter[2] <= k:
        ans += counter[2] * 2
        k -= counter[2]
    else:
        ans += k * 2
        k = 0

    if counter[1] <= k:
        ans += counter[1] * 1
        k -= counter[1]
    else:
        ans += k
        k = 0
    print(ans)


if __name__ == '__main__':
    main(real())
