a, b = map(int, input().split())
num = 1

ans = 0
while num < b:
    num += a -1
    ans += 1
print(ans)
