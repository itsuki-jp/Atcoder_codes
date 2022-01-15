from collections import defaultdict

n, q = map(int, input().split())
a = list(map(int, input().split()))
xk = [list(map(int, input().split())) for _ in range(q)]
d = defaultdict(int)
count = defaultdict(int)
for i in range(n):
    now = a[i]
    count[now] += 1
    d[(now, count[now])] = i + 1
for x, k in xk:
    if d[(x, k)] == 0:
        print(-1)
    else:
        print(d[(x, k)])
