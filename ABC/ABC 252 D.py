from collections import Counter

n = int(input())
a = list(map(int, input().split()))
count = Counter(a)
ans = 0
total = 1
for k in count.values():
    total *= k
for i in range(n):
    if count[a[i]] == 0:
        continue
    ans += total
    total //= count[a[i]]
    count[a[i]] -= 1
    total *= count[a[i]]

print(ans)
