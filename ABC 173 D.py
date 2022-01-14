n = int(input())
a = sorted(list(map(int,input().split())),reverse=True)
lst = [a[0]]
ans = 0
for i in a[1:]:
    ans += lst[-1]
    lst.append(i)
print(ans)
print(lst)