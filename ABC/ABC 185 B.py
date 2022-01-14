n,m,t = map(int,input().split())
n_org = n
past = 0
for i in range(m):
    a,b = map(int,input().split())
    n -= (a - past)
    if n <= 0:
        exit(print("No"))
    else:
        past = b
        if (b-a) + n >= n_org:
            n = n_org
        else:
            n += (b-a)
if n - (t - past) > 0:
    print("Yes")
else:
    print("No")

