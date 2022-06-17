n = int(input())
a = list(map(int, input().split()))
ans = float("inf")
for i in range(1 << (n - 1)):
    xor = 0
    num_or = a[0]
    for j in range(1, n):
        if (i >> (j - 1)) & 1:
            num_or |= a[j]
        else:
            xor ^= num_or
            num_or = a[j]
    xor ^= num_or
    ans = min(ans, xor)
print(ans)
