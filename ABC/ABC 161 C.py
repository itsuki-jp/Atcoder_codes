n, k = map(int, input().split())

a = n / k
if True:
    b = n % k
    if b == 0:
        print(0)
    else:
        c = abs(b - k)
        if b < c:
            print(b)
        else:
            print(c)
