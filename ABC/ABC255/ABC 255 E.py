# 解説

from itertools import accumulate
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
cum = [0] + list(accumulate(A))
queries = [(int(input()), i) for i in range(Q)]
queries.sort()
ans = [0] * Q
j = 0
for x, i in queries:
    while j < N and A[j] < x:
        j += 1
    ans[i] = cum[-1] - cum[j] - x * (N - j) + x * j - cum[j]
print(*ans, sep="\n")