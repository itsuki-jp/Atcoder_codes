n = int(input())
lst = [list(input())]
ans = 0
for i in lst[0]:
    if i == "x":
        ans += 1
lst = lst + [list(input()) for _ in range(n - 1)]
for i in range(1, n):
    for j in range(9):
        if lst[i][j] == "x":
            ans += 1
        if lst[i][j] == "o" and lst[i - 1][j] != "o":
            ans += 1
print(ans)
