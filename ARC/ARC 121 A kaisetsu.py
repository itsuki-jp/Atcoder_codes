from itertools import combinations

n = int(input())
x, y = [], []
for i in range(n):
    xi, yi = map(int, input().split())
    x.append([xi, i])
    y.append([yi, i])

x_sort = sorted(x)
y_sort = sorted(y)

lst = [x_sort[0][1], x_sort[-1][1], x_sort[-2][1], x_sort[1][1],
       y_sort[0][1], y_sort[-1][1], y_sort[-2][1], y_sort[1][1]]
sets = set(lst)
ans = []
for i, j in combinations(sets, 2):
    ans.append(max(abs(x[i][0] - x[j][0]), abs(y[i][0] - y[j][0])))
ans.sort()
print(ans[-2])
