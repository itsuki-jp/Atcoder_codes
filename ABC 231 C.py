import bisect

n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
for _ in range(q):
    x = int(input())
    pos = bisect.bisect_right(a, x)
    if a[pos - 1] == x:
        pos -= 1
    print(n - pos)
