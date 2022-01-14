def is_ok( x ):
    for i in range(n):
        for j in range(n):
            field[i+1][j+1] = field[i+1][j] + field[i][j+1] - field[i][j]
            if a[i][j] > x:
                field[i + 1][j + 1] += 1
    for i in range(n-k+1):
        for j in range(n-k+1):
            temp = field[i+k][j+k] - field[i][j+k] - field[i+k][j] + field[i][j]
            if temp < num:
                return True
    return False


def binary_search( ng, ok ):
    while abs(ok - ng) > 1:
        mid = (ng + ok) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
num = k ** 2 // 2 + 1
field = [[0] * (n + 1) for _ in range(n+1)]
print(binary_search(-1, 10**10))
