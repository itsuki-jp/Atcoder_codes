n, d, h = map(int, input().split())
ans = 0
dh = [list(map(int, input().split())) for _ in range(n)]
cnt = 0


def is_ok( arg ):
    for i in range(n):
        x = dh[i][0]
        y = dh[i][1]
        if (h - arg) / d * x + arg < y:
            return False

    return True

def meguru_bisect( ng, ok ,cnt):
    while cnt < 100:
        mid = (ok + ng) / 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
        cnt += 1
    return ok
print(meguru_bisect(0,1000,0))