from collections import Counter

n = int(input())
a = list(map(int, input().split()))

cnt = Counter(a)
ans = 0
for k in cnt.keys():
    num = cnt[k]
    if num >= k:
        ans += num - k
    else:
        ans += num
print(ans)