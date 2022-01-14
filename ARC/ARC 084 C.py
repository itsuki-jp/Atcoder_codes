import bisect

n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))
lst1 = []
lst2 = []
for i in range(n):
    temp1 = bisect.bisect_right(b, a[i])
    lst1.append(n - temp1)
    temp2 = bisect.bisect_right(c, b[i])
    lst2.append(n - temp2)
acc = [0]
for i in lst2[::-1]:
    acc.append(acc[-1] + i)
ans = 0
for i in lst1:
    ans += acc[i]
print(ans)
