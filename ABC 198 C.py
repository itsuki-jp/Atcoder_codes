from math import sqrt
from math import floor
from decimal import *
r,x,y = map(int,input().split())
dist = Decimal(str(sqrt(x**2 + y**2)))
ans = int(Decimal(str(dist))/Decimal(str(r)).quantize(Decimal("0"),rounding=ROUND_DOWN))
if Decimal(str(dist)) % Decimal(str(r)) == Decimal(0):
    print(ans)
else:
    print(ans + 1)