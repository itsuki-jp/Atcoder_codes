from math import log, e

lst = [90.1, 36.4, 14.8, 6, 2.3]
n1 = 0
for _ in lst:
    n1 += log(_)
print(n1 / 5)