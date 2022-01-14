def is_ok( x ):
    return x * (x + 1) // 2 <= n + 1


n = int(input())
ok = 1
ng = 10 ** 18 + 1
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid
print(n + 1 - ok)
