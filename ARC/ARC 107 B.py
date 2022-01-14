# 解説AC
def solve( x ):
    if 0 < x <= n:
        return x - 1
    elif n < x <= 2 * n:
        return 2 * n - x + 1
    else:
        return 0


n, k = map(int, input().split())
ans = 0
for x in range(2 * n + 1):
    ans += solve(x) * solve(x + k)
print(ans)
