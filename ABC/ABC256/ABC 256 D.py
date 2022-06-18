n = int(input())
lr = [list(map(int, input().split())) for _ in range(n)]
lr.sort()
ans = []
now = lr[0]
for le, ri in lr:
    if now[0] <= le <= now[1] or le <= now[0] <= ri:
        now[0] = min(now[0], le)
        now[1] = max(now[1], ri)
    else:
        ans.append(now)
        now = [le, ri]
ans.append(now)
for i in ans:
    print(*i)
