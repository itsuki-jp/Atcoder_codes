n = int(input())
a = list(map(int, input().split()))
ans = float("inf")
for i in range(1 << (n - 1)):
    xor = 0
    cur = a[0]
    for j in range(n - 1):
        if i >> j & 1:
            xor ^= cur
            cur = a[j + 1]
        else:
            cur |= a[j + 1]
    xor ^= cur
    ans = min(ans, xor)
print(ans)
