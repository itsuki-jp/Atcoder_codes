n, k = map(int, input().split())
a = list(map(int, input().split()))
if k == 1:
    exit(print("Yes"))
d = dict()  # value / index
sort_ed = sorted(a)
for i in range(n):
    if a[i] in d:
        d[a[i]].add(i)
    else:
        d[a[i]] = set()
        d[a[i]].add(i)
cnt = 0
for i in range(n):
    if i in d[sort_ed[i]]:
        d[sort_ed[i]].remove(i)
        cnt += 1
        continue
    for j in range(i, n, k):
        if j in d[sort_ed[i]]:
            d[a[i]].remove(i)
            d[a[i]].add(j)
            d[sort_ed[i]].remove(j)
            cnt += 1
            break
if cnt == n:
    print("Yes")
else:
    print("No")
