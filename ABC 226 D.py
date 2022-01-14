from math import gcd

n = int(input())
xy = []
for _ in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))
ans = set()
for i in range(n - 1):
    x1, y1 = xy[i]
    for j in range(i + 1, n):
        x2, y2 = xy[j]
        t1, t2 = x2 - x1, y2 - y1
        temp = gcd(abs(t1), abs(t2))
        t1 /= temp
        t2 /= temp
        ans.add((-t1, -t2))
        ans.add((t1, t2))
print(len(ans))
