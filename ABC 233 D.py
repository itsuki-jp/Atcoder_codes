from itertools import accumulate
from collections import Counter

n, k = map(int, input().split())
a = list(map(int, input().split()))
acc = list(accumulate(a))
count = Counter(acc)
ans = 0
total = 0
for i in range(n):
    now = acc[i] + total
    if count[-(total - a[i] + now - k)] > 0:
        ans += count[-(total - a[i] + now - k)]
    total -= a[i]
    count[acc[i]] -= 1
print(ans)
