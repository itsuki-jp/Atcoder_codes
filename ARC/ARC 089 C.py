n = int(input())
nx, ny, nt = 0, 0, 0

for i in range(n):
    t, x, y = map(int, input().split())
    n1 = abs(x - nx) + abs(y - ny)
    n2 = t - nt
    if n1 <= n2 and (n1 - n2) % 2 == 0:
        nt = t
        nx = x
        ny = y
    else:
        print("No")
        exit()
print("Yes")
