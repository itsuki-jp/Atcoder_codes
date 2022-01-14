n,m,a,b = map(int,input().split())
stock = n
for i in range(1,m+1):
    if stock <= a:
        stock += b
    c = int(input())
    if c > stock:
        print(i)
        exit()
    stock -= c
print("complete")