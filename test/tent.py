from itertools import accumulate


def is_ok( mid, now, k ):
    if A[mid + 1] - A[now] >= k:
        return True
    else:
        return False


def bisect( ng, ok, now, k ):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, now, k):
            ok = mid
        else:
            ng = mid
    return ok


N, K = map(int, input().split())
a = list(map(int, input().split()))
A = [0] + list(accumulate(a))

ans = 0
for i in range(N):
    right = bisect(i - 1, N, i, K)
    ans += N - right

print(ans)
