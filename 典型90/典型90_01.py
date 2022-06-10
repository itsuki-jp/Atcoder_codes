def is_ok( mid ):
    cnt = 0
    left = 0
    for right in a:
        if right - left >= mid:
            cnt += 1
            left = right
    if cnt >= k + 1:
        return True
    return False


def bisect( ng, ok ):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split())) + [n] + [l]
print(bisect(l, 1))
