# 解説AC
import sys

sys.setrecursionlimit(10000)


def solve( n, x ):
    if n == 0:
        return 0 if x <= 0 else 1
    mid = (As[n] + 1) // 2

    if x == mid:
        return Ps[n - 1] + 1
    elif x > mid:
        return Ps[n - 1] + 1 + solve(n - 1, x - mid)
    elif mid > x:
        return solve(n - 1, x - 1)


N, X = map(int, input().split())
As = [1]  # lviバーガーの層数
Ps = [1]  # lviバーガーのパティ数
for _ in range(N):
    As.append(2 * As[_] + 3)
    Ps.append(2 * Ps[_] + 1)
ans = solve(N, X)
print(ans)
