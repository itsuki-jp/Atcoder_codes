a,b,c=map(int,input().split())
ans = 0
for A in range(1,a+1):
    for B in range(1,b+1):
        for C in range(1,c+1):
            ans += A*B*C
print(ans)