import math


def my_lcm( x, y ):
    return (x * y) // math.gcd(x, y)


def total( a, d, n, l ):
    return n * (a + l) // 2


n, a, b = map(int, input().split())
ans = total(1, 1, n, n) - (total(1, a, n // a, a * (n // a))
                           + total(1, b, n // b, a * (n // b))
                           - total(1, my_lcm(a, b), n // my_lcm(a, b), my_lcm(a, b) * (n // my_lcm(a, b))))
t1 = total(1, 1, n, n)
t2 = total(a, a, n // a, a * (n // a))
t3 = total(b, b, n // b, b * (n // b))
t4 = total(my_lcm(a, b), my_lcm(a, b), n // my_lcm(a, b), my_lcm(a, b) * (n // my_lcm(a, b)))
print(t1-(t2+t3-t4))
