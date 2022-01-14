from collections import Counter

n = int(input())
a = list(map(int, input().split()))
d = dict()
for i in range(len(a)):
    if a[i] in d:
        temp = d[a[i]]
        d[a[i]] = [i, *temp]
    else:
        d[a[i]] = [i]
c = Counter(a)
ans = [0] * 2 ** n
if 1 not in c or c[1] != 1:
    exit(print(-1))
if 2 not in c or c[2] != 1:
    exit(print(-1))
for i in range(n, 1, -1):
    if 2 ** i not in c or c[2 ** i] != 2 ** (i - 1):
        exit(print(-1))
    temp = d[2 ** i]
    for j in range(2 ** (i - 1)):
        ans[2 ** (n - i) - 1 + j * 2 ** (n - i + 1)] = temp[j] + 1
for i in range(len(ans)):
    if ans[i] != 0:
        continue
    else:
        if c[2] != 0:
            ans[i] = 1 + d[2][0]
            c[2] = 0
        else:
            ans[i] = 1 + d[1][0]
print(*ans)
