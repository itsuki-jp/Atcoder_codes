x, a, d, n = map(int, input().split())
n -= 1
if d < 0:
    d *= -1
    x *= -1
    a *= -1
if x <= a:
    print(a - x)
elif (a + n * d) <= x:
    print(x - (a + n * d))
else:
    x -= a
    print(min(x % d, d - x % d))
