n, l, t, x = map(int, input().split())
time = 0
ans = 0
for _ in range(n):
    a, b = map(int, input().split())  # a[sec],b[weight]
    ans += a
    if l <= b:
        if a > t:
            exit(print("forever"))
        elif a + time == t:
            ans += x
            time = 0
        elif a + time > t:
            ans += x + (t - time)
            if a == t: # ぴったりだったら、a + time == t:と同じ処理をする必要がある
                ans += x
                time = 0
            else:
                time = a
        else:
            time += a
    else:
        time = 0
print(ans)
