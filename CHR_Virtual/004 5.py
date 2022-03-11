from heapq import *

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort(reverse=True)
ans = 0
h = []
for i in range(1, m + 1):
    while True:
        if len(ab) == 0:
            break
        if ab[-1][0] == i:
            d, c = ab.pop(-1)
            heappush(h, -c)
        else:
            break
    if len(h) != 0:
        ans += heappop(h)
print(ans * -1)