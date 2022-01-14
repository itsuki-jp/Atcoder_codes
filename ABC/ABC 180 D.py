import math
x,y,a,b = map(int, input().split())

n = int(math.log(b/x)/math.log(a))
if x * a**n < y:
    print((y - x * a ** n) // b + n)
else:
    print(int(math.log(y/x)/math.log(a)))
ans = 0
while x*a < y and x*a<=b+x:
    x *= a
    ans += 1
print(ans + (y-x)//b)
