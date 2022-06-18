n = int(input())
a = list(map(int, input().split()))
p = 0
lst = []
for i in range(n):
    lst.append(0)
    lst_nxt = []
    for j in lst:
        if a[i] + j >= 4:
            p += 1
            continue
        lst_nxt.append(a[i] + j)
    lst = lst_nxt
print(p)
