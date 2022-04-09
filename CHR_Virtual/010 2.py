from itertools import combinations
from math import gcd

n = int(input())
x = list(map(int, input().split()))
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
ans = float("inf")
for i in range(1, len(prime) + 1):
    for j in combinations(prime, i):
        temp = 1
        for k in j:
            temp *= k
        for k in x:
            if gcd(temp, k) == 1:
                break
        else:
            ans = min(ans, temp)
print(ans)
