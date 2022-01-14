x,n = map(int,input().split())
p = list(map(int,input().split()))
p.sort()
ans1 = 999999
for i in range(101,-1,-1):
    if i not in p:
        if abs(x - i) <= abs(x - ans1):
            ans1 = i
print(ans1)
