import math

n, m = map(int, input().split())
s = input()
t = input()
lcm = n * m / math.gcd(n, m)
if s[0] != t[0]:
    print(-1)
    exit()
if not max(n, m) // min(n, m) == max(n, m) / min(n, m):
    print(int(lcm))
else:  # 変える必要がありそう
    print(-1)
