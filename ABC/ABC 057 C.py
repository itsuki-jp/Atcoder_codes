n = int(input())
ans = 10 ** 10
for a in range(1, int(n ** 0.5) + 1):
    if n % a == 0:
        b = n // a
        num = max(len(str(a)), len(str(b)))
        if ans > num:
            ans = num
print(ans)
