import itertools
import math
n = int(input())
pattern = list(itertools.permutations(range(n)))
xy = [list(map(int,input().split())) for _ in range(n)]
n2 = 1

for i in range(1,n+1):
    n2 *=i
ans = 0
for j in pattern:
    for k in range(n-1):
        ans += ((xy[j[k+1]][0] - xy[j[k]][0])**2 + (xy[j[k+1]][1] - xy[j[k]][1])**2)**0.5

print(ans/n2)