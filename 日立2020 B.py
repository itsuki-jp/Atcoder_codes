a,b,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
min_price = min(a) + min(b)
for i in range(m):
    x,y,c = map(int,input().split())
    temp = a[x-1] + b[y-1] - c
    if temp < min_price:
        min_price = temp
print(min_price)