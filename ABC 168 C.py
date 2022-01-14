import math
a,b,h,m = map(int,input().split())

deg1 = 30 * h + 0.5*m
deg2 = 6*m
deg3 = deg2 - deg1
ans = a**2 + b**2 - (2*a*b*math.cos(math.radians(deg3)))
print(ans**0.5)
