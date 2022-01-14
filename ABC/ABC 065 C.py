n, m = map(int, input().split())
if max(n, m) > min(n, m) + 1:
    print(0)
    exit()
mod = 10 ** 9 + 7


def factorial(num):
    value = 1
    cnt = 1
    while cnt <= num:
        value = value * cnt % mod
        cnt += 1
    return value


if n == m:
    print(factorial(n) * factorial(m) % mod * 2 % mod)
else:
    print(factorial(n) * factorial(m) % mod)
