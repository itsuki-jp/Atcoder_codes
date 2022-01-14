from collections import Counter
n = int(input())
xy = sorted([list(map(int, input().split())) for _ in range(n)])
xy2 = [[xy[0]]]  # xが同じ組のリスト
for i in range(1,n):
    if xy[i][0] != xy[i - 1][0]:
        xy2.append([])
    xy2[-1].append(xy[i])
lst1 = []  # Length
sets = set()
lst2 = []  # pos(y)
for i in xy2:
    if len(i) < 2:
        continue
    for j in range(len(i) - 1):
        for k in range(j + 1,len(i)):
            if i[j][1] - i[k][1] in sets:
                pos = lst1.index(i[j][1] - i[k][1])
                lst2[pos].append(i[j][1])
            else:
                sets.add(i[j][1] - i[k][1])
                lst1.append(i[j][1] - i[k][1])
                lst2.append([])
                lst2[-1].append(i[j][1])
ans = 0
for i in lst2:
    c = Counter(i)
    for j in c.values():
        ans += max(0,j * (j - 1) // 2)
print(ans)
