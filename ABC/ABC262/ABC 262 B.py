n, m = map(int, input().split())
grid = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    u, v = [int(_) - 1 for _ in input().split()]
    grid[u][v] = 1
    grid[v][u] = 1
ans = 0
for a in range(n - 2):
    for b in range(a + 1, n - 1):
        for c in range(b + 1, n):
            if grid[a][b] == grid[b][c] == grid[c][a] == 1:
                ans += 1
print(ans)
