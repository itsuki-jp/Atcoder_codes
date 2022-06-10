n = int(input())
y = {}
for _ in range(n):
    xt, yt = map(int, input().split())
    if yt in y:
        y[yt].append((xt, _))
    else:
        y[yt] = [(xt, _)]
s = input()
for i in y.values():
    l, r = 0, 0
    ll, rr = -10 ** 10, 10 ** 10
    for j in i:
        if s[j[1]] == "L":
            l += 1
            ll = max(ll, j[0])
        else:
            r += 1
            rr = min(rr, j[0])
    if l and r and rr <= ll:
        print("Yes")
        exit()
print("No")
