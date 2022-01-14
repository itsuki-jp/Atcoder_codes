n = int(input())
mx1 = int(pow(n, 1/3)) + 10
ans = 0
for a in range(1, mx1):
    mx2 = int(pow(int(n / a) + 1, 1 / 2)) + 110
    for b in range(a, mx2):
        ab = a * b
        if a * b * b > n:
            continue
        ans += n // ab - (b - 1)
print(ans)

