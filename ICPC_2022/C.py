from math import pow, ceil

while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    ans = -float("inf")
    for i in range(min(n,m)):
        plus = pow(n - i, 2) + i
        minus = pow(m // (i + 2), 2) * (m // (m // (i + 2))) + pow(ceil(m // (i + 2)), 2) * (m - (m // (m // (i + 2))))
        ans = max(plus - minus, ans)
    print(ans)
