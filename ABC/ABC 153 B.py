import math
import itertools

n, d = map(int, input().split())
x = []
a = []
for i in range(n):
    xi = list(map(int, input().split()))
    x.append(xi)
    a.append(i)

all_pattern = list(itertools.combinations(a, 2))
ans = 0
for i in range((n * (n - 1)) // 2):
    x1 = x[all_pattern[i][0]]
    x2 = x[all_pattern[i][1]]
    distance = 0
    for j in range(d):
        distance += ((x1[j] - x2[j]) ** 2)
    if math.sqrt(distance) == int(math.sqrt(distance)):
        ans += 1
print(ans)
