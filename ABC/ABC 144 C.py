import math

n = int(input())
ans_min = 10 ** 13
for i in range(1, int(math.sqrt(n)) + 1):
    a, b = divmod(n, i)
    if b == 0:
        ans = a + i - 2
        if ans_min > ans > 0:
            ans_min = ans
print(ans_min)
