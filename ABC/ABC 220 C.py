from itertools import accumulate
import bisect


def is_ok( num ):
    if x - total * num >= total:
        return False
    else:
        return True


def meguru_bisect( ng, ok ):
    while abs(ok - ng) > 1:  # 少数の場合は、cntとか作って、cnt < 100とか
        mid = (ok + ng) // 2  # 小数の場合は、mid = (ok + ng) / 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


n = int(input())
a = list(map(int, input().split()))
x = int(input())
lst = list(accumulate(a))
total = lst[-1]
bis = meguru_bisect(-1, 10 ** 20)
num = x - total * bis
print(bis * n + bisect.bisect_right(lst, num) + 1)
