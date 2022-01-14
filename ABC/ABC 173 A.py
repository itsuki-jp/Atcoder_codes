n = int(input())
a,b = divmod(n,1000)
if b == 0:
    print(0)
else:

    print(1000-b)