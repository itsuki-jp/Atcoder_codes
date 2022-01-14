r, g, b, n = map(int, input().split())
ans = 0
for i in range((n//r)+1):
    for j in range((n//g)+1):
        temp = (n - i * r - j * g)
        if temp >=0 and temp % b == 0:
            ans += 1
print(ans)
