n, c, k = map(int, input().split())
t = sorted([int(input()) for _ in range(n)])
cnt = 1
ans = 1
time = [t[0], t[0] + k]
for i in t[1:]:
    if cnt < c:
        if time[0] <= i <= time[1]:
            cnt += 1
        else:
            cnt = 1
            ans += 1
            time = [i, i + k]
    else:
        cnt = 1
        ans += 1
        time = [i, i + k]
print(ans)
