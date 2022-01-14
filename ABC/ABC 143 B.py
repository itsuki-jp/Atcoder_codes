n = int(input())
d = list(map(int,input().split()))
ans = 0
for i in range(n-1):
    for j in range(1,n):
        if j > i:
            ans += d[i] * d[j]
print(ans)