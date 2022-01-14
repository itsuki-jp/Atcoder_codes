x,k,d = map(int,input().split())
x = abs(x)
if k*d <= x:
    print(x - k*d)
else:
    if (k - x//d) %2 == 0:
        print(x%d)
    else:
        print(abs(x%d-d))