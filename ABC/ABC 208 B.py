import math

money = [math.factorial(i) for i in range(1, 11)][::-1]
ans = 0
p = int(input())
for i in money:
    if p == 0:
        print(ans)
        exit()
    ans += p // i
    p %= i
print(ans)