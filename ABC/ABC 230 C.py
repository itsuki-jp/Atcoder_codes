n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())
ans = [["." for _ in range(s - r + 1)] for _ in range(q - p + 1)]
for i in range(q - p + 1):
    y = i + p
    for j in range(s - r + 1):
        x = j + r
        if abs(a - y) == abs(b - x):
            ans[i][j] = "#"
for _ in ans:
    print(*_, sep="")
