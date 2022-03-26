from math import pi

a, b, c = [int(_) for _ in input().split()]
ans = (a + b + c) * (a + b + c) * pi
if a > b + c:
    ans -= (a - b - c) * (a - b - a) * pi
print(ans)
