n = int(input())
ans = 1
for i in range(2, n + 1):
    ans *= i
ans += 1
cnt = n + 1

while ans < 10 ** 13:
    for j in range(2,n+1):
        if ans < 10**13 and ans % j != 1:
            ans -= 1
            ans *= cnt
            ans += 1
            break
    else:
        exit(print(ans))
