x1, y1, x2, y2 = map(int, input().split())
ans = "No"
for c_x, c_y in [(1, 2), (2, 1), (2, 1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
    nx, ny = x1 - c_x, y1 - c_y
    if (x1 - nx) ** 2 + (y1 - ny) ** 2 == (x2 - nx) ** 2 + (y2 - ny) ** 2 == 5:
        exit(print("Yes"))
print("No")
