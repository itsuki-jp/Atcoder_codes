n = int(input())
pre = []
for i in range(n):
    a = []
    for j in range(i + 1):
        if j == 0 or j == i:
            a.append(1)
        else:
            a.append(pre[j - 1] + pre[j])
    print(*a)
    pre = a[::1]
