n, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab = sorted(ab)
now = 0
for i in ab:
    a, b = i[0], i[1]
    if k >= a - now:
        k -= (a - now)
        now = a
        k += b
    else:
        print(now + k)
        exit()
print(min(10**100 - 1,now + k))