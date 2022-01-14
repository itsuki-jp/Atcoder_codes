n = int(input())
ans= 0
for i in range(n):
    a,b = map(int, input().split())
    ans += 0.5*b*(b+1)-(0.5*(a-1)*(a))
print(int(ans))
