import sys

b, c = map(int, input().split())
b1_mn = b - c // 2
b1_mx = b + (c - 1) // 2
b2_mn = -b - max(0, (c - 2) // 2)
b2_mx = -b + (c - 1) // 2

print("b1_mn :", b1_mn, file=sys.stderr)
print("b1_mx :", b1_mx, file=sys.stderr)
print("b2_mn :", b2_mn, file=sys.stderr)
print("b2_mx :", b2_mx, file=sys.stderr)

tot = 0
if b1_mn <= b2_mx and b2_mn <= b1_mx:
    print("overlap", file=sys.stderr)
    tot = max(b1_mx, b2_mx) - min(b1_mn, b2_mn) + 1
else:
    tot = (b1_mx - b1_mn + 1) + (b2_mx - b2_mn + 1)
print(tot)
