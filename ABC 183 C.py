import itertools
n,k = map(int,input().split())
t = [list(map(int,input().split())) for _ in range(n)]

lst1 = [i for i in range(1,n)]
lst2 = list(itertools.permutations(lst1, n-1))
for i in range(len(lst2)):
    temp = [0] + list(lst2[i]) + [0]
    lst2[i] = temp
ans = 0
for i in lst2:
    count = 0
    now = 0
    for j in i:
        count += t[now][j]
        now += 1
    if count == k:
        ans+= 1
    print(count)
print(ans)