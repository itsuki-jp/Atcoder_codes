import bisect

n = int(input())
l = sorted(list(map(int, input().split())))
ans = 0
for ai in range(n-2):
    for bi in range(ai + 1,n-1):
        a = l[ai]
        b = l[bi]
        # abs(a-b) < c  < a + b
        low = abs(a - b)
        high = a + b
        low_val = bisect.bisect_left(l,low, bi + 1)
        high_val = bisect.bisect_left(l, high, bi + 1)
        if high_val - low_val >= 0:
            ans += high_val - low_val
print(ans)