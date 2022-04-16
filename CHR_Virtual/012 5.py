from itertools import accumulate

n, k = map(int, input().split())
a = list(map(int, input().split()))
while True:
    now = [0 for _ in range(n)]
    temp = [0 for _ in range(n)]
    for x in range(n):
        now[min(max(0, x - a[x]), n - 1)] += 1
        now[min(n - 1, x + a[x])] -= 1
    acc = list(accumulate(now))
    if a == acc:
        exit(print(*acc))
    a = acc[::1]
