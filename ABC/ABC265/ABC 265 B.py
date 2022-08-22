n, m, t = map(int, input().split())
a = list(map(int, input().split()))
bonus = {}
for _ in range(m):
    x, y = map(int, input().split())
    bonus[x - 1] = y
pos = 0
while pos != (n - 1):
    if pos in bonus:
        t += bonus[pos]
    if t > a[pos]:
        t -= a[pos]
        pos += 1
        continue
    print("No")
    exit()
print("Yes")
