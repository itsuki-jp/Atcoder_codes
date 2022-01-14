ans = 0
for i in range(20):
    a = list(map(int, input().split()))
    for j in a:
        if j == 1:
            continue
        for k in range(2, int(j ** 0.5) + 1):
            if j % k == 0:
                break
        else:
            ans += 1
print(ans)
