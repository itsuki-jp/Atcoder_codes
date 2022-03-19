def prime( n ):
    f = []
    b = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            f.append(i)
            if not i * i == n:
                b.append(n // i)
    return [*f, *b[::-1]]


a, b = map(int, input().split())
a = prime(a)
b = set(prime(b))
ans = -1
for ai in a:
    if ai in b:
        ans = max(ans, ai)
print(ans)
