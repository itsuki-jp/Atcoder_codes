import collections
n = int(input())
a = list(map(int, input().split()))
col = collections.Counter(a)
lst1 = list(col.keys())
lst2 = list(col.values())
ans = 0
for i in range(n - 1):
    num = a[i]
    if col[num] == 0:
        ans += n - i + 1
        col[num] -= 1
    else:
        ans += n - i + 1 - col[num] - 1
        col[num] -= 1
print(ans)
