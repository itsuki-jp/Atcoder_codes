from itertools import combinations
n = int(input())
abcde = [[i+1] + list(map(int, input().split())) for i in range(n)]
ans = 0
a = sorted(abcde,reverse=True, key=lambda x: x[1])[:3]
b = sorted(abcde,reverse=True, key=lambda x: x[2])[:3]
c = sorted(abcde,reverse=True, key=lambda x: x[3])[:3]
d = sorted(abcde,reverse=True, key=lambda x: x[4])[:3]
e = sorted(abcde,reverse=True, key=lambda x: x[5])[:3]
abced = a + b + c + d + e
for comb in list(combinations(abcde,3)):
    x = comb[0]
    y = comb[1]
    z = comb[2]
    if x[0] != y[0] != z[0]:
        amax = max(x[1],y[1],z[1])
        bmax = max(x[2], y[2], z[2])
        cmax = max(x[3], y[3], z[3])
        dmax = max(x[4], y[4], z[4])
        emax = max(x[5], y[5], z[5])
        temp = min(amax,bmax,cmax,dmax,emax)
        ans = max(temp,ans)
print(ans)
