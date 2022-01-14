step = int(input())
n = int(input())
a = list(map(int, input().split()))
if step == 1:
    ans1 = 0
    for i in range(1, n):
        ans1 = max(ans1, i * (n - i))
    print(ans1)
if step == 2:
    ans2 = 0
    for i in range(1, 2 ** n):
        tree = 0
        temp2 = 0
        for j in range(n):
            if (i >> j) & 1:
                tree += a[j]
            else:
                temp2 += tree
        ans2 = max(ans2, temp2)
    print(ans2)
if step == 3:
    pass
