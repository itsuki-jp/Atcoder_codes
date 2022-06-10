def solve( h, cnt ):
    global ans
    if h == n:
        if cnt == x:
            ans += 1
        return
    for i in lst[h]:
        temp = cnt * i
        if temp > x:
            continue
        solve(h + 1, temp)


n, x = map(int, input().split())
lst = []
for _ in range(n):
    la = list(map(int, input().split()))
    lst.append(la[1:])
ans = 0
solve(0, 1)
print(ans)
