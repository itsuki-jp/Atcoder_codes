n, w = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort()
ans = 0
while True:
    if len(ab)==0:
        break
    a, b = ab.pop()
    if b > w:
        ans += a * w
        break
    else:
        ans += a * b
        w -= b
print(ans)
