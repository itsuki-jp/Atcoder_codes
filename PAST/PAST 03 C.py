a,r,n = map(int,input().split())
ans = a
for i in range(n-1):
    ans *= r
    if ans > 10**9:
        print("large")
        exit()
print(ans)