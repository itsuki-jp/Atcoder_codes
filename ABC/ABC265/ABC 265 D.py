from itertools import accumulate
from bisect import *

n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))

acc = [0] + list(accumulate(a))
for pos_x in range(len(acc)):
    val_x = acc[pos_x]

    pos_y = bisect_left(acc, val_x + p, lo=pos_x)
    if pos_y == len(acc):
        continue
    val_y = acc[pos_y]

    pos_z = bisect_left(acc, val_y + q, lo=pos_y)
    if pos_z == len(acc):
        continue
    val_z = acc[pos_z]

    pos_w = bisect_left(acc, val_z + r, lo=pos_z)
    if pos_w == len(acc):
        continue
    val_w = acc[pos_w]

    if val_y - val_x == p and val_z - val_y == q and val_w - val_z == r:
        print("Yes")
        exit()
print("No")
