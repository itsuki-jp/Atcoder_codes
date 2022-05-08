import math
from functools import reduce


def my_lcm_base( x, y ):
    return (x * y) // math.gcd(x, y)


def my_lcm( *numbers ):
    return reduce(my_lcm_base, numbers, 1)


n = int(input())
a = list(map(int, input().split()))
mod = my_lcm(*a) - 1
ans = 0
for _ in a:
    ans += mod % _
print(ans)
