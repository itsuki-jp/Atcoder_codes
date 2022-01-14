n,k = map(int,input().split())
r = sorted(list(map(int, input().split())))
b = 0
for i in r[n-k::]:
    b = (b+i)/2
print(b)