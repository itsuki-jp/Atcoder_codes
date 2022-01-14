n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
for i in range(n):
    if b[i] > a[i]:
        ans += a[i]
        b[i] -= a[i]
        a[i] = 0
        if a[i+1] - b[i] >=0:
            a[i+1] -= b[i]
            ans += b[i]
        elif a[i+1] - b[i] < 0:
            ans += a[i+1]
            a[i+1] = 0
    else:
        ans += b[i]
        a[i] -= b[i]
print(ans)