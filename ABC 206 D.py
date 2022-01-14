n = int(input())
a = list(map(int, input().split()))
ar = a[::-1]
lst1 = []
lst2 = []
for i in range(n):
    if a[i] != ar[i]:
        lst1.append(a[i])
        lst2.append(ar[i])
if len(set(lst1)) == 0:
    print(0)
else:
    print(len(set(lst1)) - 1)
