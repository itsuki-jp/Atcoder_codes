n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n - 1):
    l1 = lst[i][1]
    r1 = lst[i][2]
    if lst[i][0] == 2:
        r1 -= 0.5
    elif lst[i][0] == 3:
        l1 += 0.5
    elif lst[i][0] == 4:
        l1 += 0.5
        r1 -= 0.5
    for j in range(i + 1, n):
        l2 = lst[j][1]
        r2 = lst[j][2]
        if lst[j][0] == 2:
            r2 -= 0.5
        elif lst[j][0] == 3:
            l2 += 0.5
        elif lst[j][0] == 4:
            l2 += 0.5
            r2 -= 0.5
        ans += min(r2, r1) - max(l1, l2) >= 0
print(ans)
