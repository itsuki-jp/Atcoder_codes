n = int(input())
a = [0] + list(map(int, input().split()))
if n == 1:
  if a[1] > a[2]:
    exit(print(2))
  else:
    exit(print(1))
a_org = a
for i in range(1, n):
    lst = []
    ans = []
    for j in range(1, 2 ** (n - i)+1):
        if a[2 * j - 1] > a[2 * j]:
            lst.append(a[2 * j - 1])
            ans.append(a_org.index(a[2 * j - 1]))
        else:
            lst.append(a[2 * j])
            ans.append(a_org.index(a[2 * j]))
    a = [0] + lst

if a[1] > a[2]:
    print(ans[1])
else:
    print(ans[0])
