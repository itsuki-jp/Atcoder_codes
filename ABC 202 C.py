n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
aLst = [[0,0] for _ in range(10**5+1)]
bLst = [[0,0] for _ in range(10**5+1)]
cLst = [[0,0] for _ in range(10**5+1)]
ans = 0
for i in range(n):
    aLst[a[i]][0] += 1
    aLst[b[i]][1] = i
    bLst[b[i]][0] += 1
    bLst[b[i]][1] = i
    cLst[c[i]][0] += 1
    cLst[c[i]][1] = i
for i in range(10**5):
    if aLst[i][0] != 0 and bLst[i][0] != 0:
        if aLst[i][1] != 0 and cLst[bLst[i][1]] != 0:
            ans += (aLst[i][0] * bLst[i][0])
print(ans)

