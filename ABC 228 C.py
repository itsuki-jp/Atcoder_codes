from collections import defaultdict
import bisect

n, k = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]
score_lst = []
d_num = defaultdict(int)
for i in range(n):
    total = sum(p[i])
    score_lst.append(total)
    d_num[i] = total
score_lst.sort()
for i in range(n):
    total = d_num[i]
    pos = bisect.bisect_left(score_lst, total)
    if n - pos <= k:
        print("Yes")
        continue
    if score_lst[n - k] <= total + 300:
        print("Yes")
    else:
        print("No")