a,b = map(int,input().split())
d = list(map(int,input().split()))
usable = [i for i in range(10)]
for i in d:
    if i in usable:
        usable.remove(i)

for i in usable:
    for j in usable:
        for k in usable:
            for l in usable:
                for m in usable:
                    for n in usable:
                        ans = 100000*i + 10000*j + 1000*k + 100*l + 10*m + n
                        if ans >a:
                            print(ans)
                            exit()