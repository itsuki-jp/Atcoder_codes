import math
n, m = map(int, input().split())
a = [1] + sorted(list(map(int, input().split()))) + [n + 1]
length = [0]*(m+1)
for i in a:
    k = min(i - temp, k)
    temp = i
ans = 0
temp = 1
for i in a:
    ans += math.ceil((i-temp) / k)
print(ans)