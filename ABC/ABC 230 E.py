def is_ok( i ):
    global x
    if int(N // i) >= x:
        return True
    return False


def bisect( ng, ok ):
    while abs(ok - ng) > 1:  # 少数の場合は、cntとか作って、cnt < 100とか
        mid = (ok + ng) // 2  # 小数の場合は、mid = (ok + ng) / 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


#  N = int(input())
N = 10
ans = N
l = 1
for x in range(1, int(N ** 0.5) + 1):
    temp = bisect(l - 1, N + 1)
    ans += x * (temp)
    l = temp
print(ans)
