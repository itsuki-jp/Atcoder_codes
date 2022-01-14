n,d = map(int, input().split())
ans = 0
d = d * d
for i in range(n):
    x,y = map(int, input().split())
    if x**2 + y**2 <= d:
        ans += 1
print(ans)