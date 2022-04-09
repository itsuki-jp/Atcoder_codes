from heapq import *

h = [_ for _ in range(1, 11)]
heapify(h)
k = int(input())
cnt = 0
while cnt < k:
    n = heappop(h)
    cnt += 1
    if n % 10 != 0:
        heappush(h, 10 * n + n % 10 - 1)
    if n % 10 != 9:
        heappush(h, 10 * n + n % 10 + 1)
    heappush(h, 10 * n + n % 10)
print(heappop(h))
