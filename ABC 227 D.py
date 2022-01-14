def is_ok( num ):
    total = 0
    for ai in a:
        total += min(ai, num)
    if num * k > total:
        return False
    return True


def bisect( ng, ok ):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


n, k = map(int, input().split())
a = list(map(int, input().split()))
print(bisect(10 ** 20, -1))
