n, l = map(int, input().split())
lst = [0] * n
lst2 = [0] * n
for i in range(n):
    lst[i] = l + i
    lst2[i] = abs(l + i)
if 0 in lst:
    print(sum(lst))
else:
    temp = min(lst2)
    if temp in lst:
        print(sum(lst) - temp)
    else:
        print(sum(lst) + temp)
