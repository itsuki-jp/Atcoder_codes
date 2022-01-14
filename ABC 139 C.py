n = int(input())
a = list(map(int,input().split()))
temp = 0
ans = 0
for i in range(n - 1):
    if a[i] >= a[i+1]:
        temp +=1
        ans = max(ans,temp)
    else:
        temp = 0
print(ans)
