def solve( chara, pos, t ):
    rule = {"A": "BC", "B": "CA", "C": "AB"}
    for i in range(t):
        mid = pow(2, t - 2 - i)
        chara = rule[chara]
        if mid < pos:
            chara = chara[1]
            pos -= mid
        else:
            chara = chara[0]
    return chara


def main():
    s = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        k -= 1
        if t >= 60:
            origin = 0
        else:
            origin = k // pow(2, t)
        chara = s[origin]
        pos = k % pow(2, t)
        ans = solve(chara, pos, t)
        print(ans)


if __name__ == '__main__':
    main()
