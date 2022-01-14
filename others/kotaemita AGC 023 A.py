from collections import Counter
n = int(input())
a = list(map(int,input().split()))
list_sum = [0]*(len(a)+1)
for i in range(n):
    list_sum[i + 1] = list_sum[i] + a[i]
c = Counter(list_sum)
ans = 0
for v in c.values():
    if v >= 2:
        ans += v*(v-1)//2
print(ans)