h,w = map(int,input().split())
grid = [list(input().split()) for _ in range(h)]
new_grid = []
for i in range(h):
    if set(grid[i]) != set("#"):
        new_grid.append(grid[i])
    else:
        h -= 1
grid = new_grid
new_grid = []
grid = list(zip(*grid[::-1]))[0]
for j in range(w):
    if grid[j] != "#" * w:
        new_grid.append(grid[j])
    else:
        w -= 1
print(*new_grid)