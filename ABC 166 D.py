import itertools
"""
n = 1
while n**5 < 10**9:
  n += 1
print(n)
# 64
"""
X = int(input())

for a in range(-128,128):
    for b in range(-128,128):
        if a ** 5 - b ** 5 == X:
            print(a, b)
            exit()