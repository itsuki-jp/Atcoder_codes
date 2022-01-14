h,w,k = map(int,input().split())
c = [list(input()) for _ in range(h)]
ans = 0
for i in range(2**h):
    lst1 = []
    for y in range(h):
        if i >> y & 1:
            lst1.append(c[y])
    for j in range(2**w):
        lst2 = []
        for x in range(w):
            if j >> x & 1:
                for l in range(len(lst1)):
                    lst2.append(lst1[l][x])
        if lst2.count("#") == k:
            ans += 1
print(ans)