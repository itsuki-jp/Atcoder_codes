"""a, b, k = map(int, input().split())
for i in range(k):
    if a > 0:
        a -= 1
    elif b > 0:
        b -= 1
print(a, b)
"""

a, b, k = map(int, input().split())
if k - a > 0:
    k -= a
    if b - k >= 0:
        print(0, b - k)
    else:
        print("0 0")
else:
    print(a - k, b)
