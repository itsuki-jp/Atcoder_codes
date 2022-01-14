import bisect

n, m = map(int, input().split())
a = [[]for _ in range(10 ** 5 + 1)]
b = [[]for _ in range(10 ** 5 + 1)]
for i in range(m):
    pt, yt = map(int, input().split())
    a[i] = [pt,yt]
    b[pt].append(yt)
for i in range(len(b)):
    b[i].sort()
for i in range(m):
    num1 = str(a[i][0])
    num2 = str(bisect.bisect_left(b[a[i][0]],a[i][1]) + 1)
    print(num1.zfill(6)+num2.zfill(6))
