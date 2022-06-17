n, k = map(int, input().split())
a = [int(_) - 1 for _ in input().split()]
xy = [list(map(int, input().split())) for _ in range(n)]
lst = [[] for _ in range(n)]
for i in a:
    for j in range(n):
        if i == j:
            lst[j].append(0)
            continue
        lst[j].append(((xy[j][0] - xy[i][0]) ** 2 + (xy[j][1] - xy[i][1]) ** 2) ** 0.5)
ans = 0
for i in lst:
    if len(i) == 0:
        continue
    ans = max(min(i), ans)
print(ans)

"""
4 4
1 2 3 4
0 0
0 1
1 2
2 0
"""
