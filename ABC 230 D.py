n, d = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(n)]
lr.sort(key=lambda x: x[1])
ans = 0
last = 0
for (l, r) in lr:
    if last < l:
        ans += 1
        last = r + d - 1
print(ans)
