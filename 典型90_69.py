def solve():
    n, k = map(int, input().split())
    mod = 10 ** 9 + 7
    if n - 1 == 0:
        return 0
    ans = k % mod * (k - 1) % mod * pow(k - 2, n - 2, mod) % mod
    return ans


print(solve())
