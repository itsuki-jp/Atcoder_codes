def is_ok(n):
    if x >= a * n + b * len(str(n)):
        return True
    return False


def meguru_bisect(ng, ok):
    while abs(ok - ng) > 1:  # 少数の場合は、cntとか作って、cnt < 100とか
        mid = (ok + ng) // 2  # 小数の場合は、mid = (ok + ng) / 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


a, b, x = map(int, input().split())
print(meguru_bisect(10 ** 9 + 1, 0))
