a, b, c, d = map(int, input().split())
r = 0
ans = 0
for _ in range(10**6):
    if not a > r * d:
        exit(print(ans))
    ans += 1
    a += b
    r += c
print(-1)
