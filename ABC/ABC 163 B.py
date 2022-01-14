n,m = map(int,input().split())

a = list(map(int,input().split()))

work = 0
for i in a:
    work+=i
if work > n:
    print("-1")
else:
    print(n - work)