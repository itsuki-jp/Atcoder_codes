h, w, y, x = map(int, input().split())
x, y = x - 1, y - 1
s = [input() for _ in range(h)]
if s[y][x] == ".":
    ans = -3
else:
    ans = 0
xl = s[y]
for i in range(x, w):
    if xl[i] == ".":
        ans += 1
    else:
        break
for i in range(x, -1, -1):
    if xl[i] == ".":
        ans += 1
    else:
        break
yl = [s[i][x] for i in range(h)]
for j in range(y,h):
    if yl[j] == ".":
        ans += 1
    else:
        break
for j in range(y, -1, -1):
    if yl[j] == ".":
        ans += 1
    else:
        break
print(ans)