# CHR_Virtual_08
n = int(input())
s = input()
d = [1, 0]  # x,y
dd = [[1, 0], [0, -1], [-1, 0], [0, 1]]
now = [0, 0]
for i in s:
    if i == "S":
        now = [now[_] + d[_] for _ in range(2)]
    else:
        pos = dd.index(d)
        d = dd[(pos + 1) % 4][::1]
print(*now)
