import math
n = int(input())
if n == 1:
    exit(print(0))
ans = 0
cnt = 1
while True:
    if cnt == n:
        print(ans)
        exit()
    if cnt >= n:
        print(ans - 1)
        exit()
    ans += 1
    cnt *= 2
