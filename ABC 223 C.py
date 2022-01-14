from bisect import bisect_left

n = int(input())
time = [0]
dist = [0]
ab = []
eps = 10 ** -5
for _ in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])
    time.append(time[-1] + a / b)
    dist.append(dist[-1] + a)
#  print(time)
mid = time[-1] / 2
b_mid = bisect_left(time, mid)
#  print(b_mid)
if abs(time[b_mid] - mid) <= eps:
    print(dist[b_mid])
else:
    print(dist[b_mid - 1] + (mid - time[b_mid - 1]) * ab[b_mid - 1][1])
