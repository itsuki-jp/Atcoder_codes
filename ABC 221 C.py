from itertools import combinations
from collections import Counter

s = list(input())
l = len(s)
c = Counter(s)
ans = 0
for i in range(1, l // 2 + 1):
    for j in combinations(s, i):
        temp = []
        j_temp = Counter(j)
        for k in range(10):
            if c[str(k)] > j_temp[str(k)]:
                aptemp = [str(k)] * (c[str(k)] - j_temp[str(k)])
                temp.extend(aptemp)
        num = int("".join(sorted(j, reverse=True))) * int("".join(sorted(temp, reverse=True)))
        if num > ans:
            ans = num
print(ans)
