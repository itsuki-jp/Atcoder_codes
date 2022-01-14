n,x = map(int,input().split())
a = list(map(int,input().split()))
money = 0
for i in range(n):
    if (i + 1) % 2 == 0:
        money += a[i] - 1
    else:
        money += a[i]
if money <= x:
    print("Yes")
else:
    print("No")