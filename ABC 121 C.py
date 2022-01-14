n,m = map(int,input().split())
lst = []
ans = 0
for _ in range (n):
    ab = list(map(int,input().split()))
    lst.append(ab)
lst = sorted(lst)
for i in lst:
    if i[1] >= m:
        print(ans + i[0] * m)
        exit()
    else:
        ans += i[0] * i[1]
        m -= i[1]