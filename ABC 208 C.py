n, k = map(int, input().split())
a = list(map(int, input().split()))
every = k // n
remain = k % n
some = 0
if remain != 0:
    some = 1
asort = sorted(a)
sets = set(asort[:remain])
for i in a:
    if i in sets:
        print(every + some)
    else:
        print(every)
