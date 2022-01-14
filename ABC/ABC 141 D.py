import bisect

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
m_copy = m
for i in range(m):
    a[-1] //= 2
    insert_index = bisect.bisect_left(a, a[-1])
    a.insert(insert_index, a.pop(-1))
print(sum(a))

import heapq

n, m = map(int, input().split())
a = list(map(lambda x: x * (-1), list(map(int, input().split()))))
heapq.heapify(a)
for i in range(m):
    mx = heapq.heappop(a) * (-1) // 2
    heapq.heappush(a, -1 * mx)
print(-1 * sum(a))
