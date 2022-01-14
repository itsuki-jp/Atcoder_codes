a,b,c,d = map(int,input().split())
if a == 0 and a!=b:
    a += 1
if b == 0 and a!=b:
    b -= 1
if c == 0 and c!=d:
    c += 1
if d == 0 and c!=d:
    d -= 1
num1 = a*c
num2 = a*d
num3 = b*c
num4 = b*d
print(max(num1,num2,num3,num4))