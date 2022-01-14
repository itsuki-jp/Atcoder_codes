n = int(input())
a = list(map(int, input().split()))
lst = [0] * 201
for i in a:
    temp = i % 200
    lst[temp] += 1
import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
ans = 0
for i in lst:
    if i >1:
        temp = combinations_count(i,2)
        ans += temp
print(ans)