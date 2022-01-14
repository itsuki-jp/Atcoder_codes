n, m = map(int, input().split())
lst = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        ans = 0
        if lst[i][j] == "#":
            ans += 1
        if i != n - 1:
            if lst[i + 1][j] == "#":
                ans += 1
            if j != m - 1 and lst[i + 1][j + 1] == "#":
                ans += 1
            if j != 0 and lst[i + 1][j - 1] == "#":
                ans += 1
        if i != 0:
            if lst[i - 1][j] == "#":
                ans += 1
            if j != 0 and lst[i - 1][j - 1] == "#":
                ans += 1
            if j != m - 1 and lst[i - 1][j + 1] == "#":
                ans += 1
        if j != m - 1 and lst[i][j + 1] == "#":
            ans += 1
        if j != 0 and lst[i][j - 1] == "#":
            ans += 1
        print(ans, end="")
    print()
