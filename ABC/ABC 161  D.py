k=int(input())

if k <= 12:
    print(k)
    exit()
number = k-12
a,b = divmod(number,3)
if b==0:
    b=3
elif b==1:
    b=2
else:
    b=3
print(str(a+1)+str(b))

for i in range(k):
