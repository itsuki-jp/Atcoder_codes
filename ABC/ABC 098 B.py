n = int(input())
s = list(input())
ans = 0
if n == 2:
    print(1 if len(set(s)) == 1 else 0)
    exit()

for i in range(1, n - 1):
    num = 0
    lst1 = list(set(s[:i]))
    lst2 = list(set(s[i:]))
    if len(lst1) < len(lst2):
        lst1,lst2 = lst2,lst1
    for j in range(len(lst1)):
        for k in range(len(lst2)):
            if lst1[j] == lst2[k]:
                num += 1
    ans = max(ans,num)
print(ans)