a, b, k = map(int, input().split())
ans = 0
while True:
    if a >= b:
        print(ans)
        break
    ans += 1
    a *= k
