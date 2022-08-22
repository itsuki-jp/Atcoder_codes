x, y, n = map(int, input().split())
ans = float("inf")
for i in range(101):
    for j in range(101):
        if i + 3 * j == n:
            ans = min(ans, x * i + y * j)
print(ans)
