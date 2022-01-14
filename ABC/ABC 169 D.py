def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


import collections

n = int(input())
if n == 1:
    exit(print(0))
lst = collections.Counter(prime_factorize(n)).items()
ans = 0
for i in lst:
    num = i[1]
    cnt = 1
    while True:
        ans += 1
        cnt += 1
        num -= cnt
        if num < 0:
            break
print(ans)
