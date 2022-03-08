t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())  # length = 2,3,4
    ans = 0
    use3 = b // 2
    # 3を使い切る
    if c >= use3:
        ans += use3
        c -= use3
    else:
        ans += c
        use3 -= c
        if a // 2 >= use3:
            ans += use3
            a -= use3 * 2
        else:
            ans += a // 2
    #  4を使い切る
    use4 = c // 2
    if a >= use4:
        ans += use4
        a -= use4
    else:
        ans += a
