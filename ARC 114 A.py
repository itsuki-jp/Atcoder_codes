from math import gcd
n = int(input())
x = list(map(int, input().split()))
p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
l = len(p)
ans = float('inf')
for i in range(2 ** l):
    temp = 1
    for j in range(l):
        if (i >> j) & 1:
            temp *= p[j]
    if all([gcd(temp, i) > 1 for i in x]):
        ans = min(temp, ans)
print(ans)
