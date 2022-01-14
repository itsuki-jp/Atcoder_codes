import math
n,m = map(int,input().split())
n2 = n*(n-1)/2
m2 = m*(m-1)/2

print(round(n2+m2))

"""
if n == 1 :
    print(math.factorial(m-1))
elif m ==1:
    print(math.factorial(n-1))
else:
    print(math.factorial(n-1)+math.factorial(m-1))
"""

"""if n==1:
    if m==1:
        print("0")
    elif m ==2:
        print("1")
    else:
        print(math.factorial(m))
elif n==2:
    if m==1:
        print("1")
    elif m ==2:
        print("2")
    else:
        print(math.factorial(m)+1)
elif m==1:
    if n==1:
        print("0")
    elif n ==2:
        print("1")
    else:
        print(math.factorial(n))
elif m==2:
    if n==1:
        print("1")
    elif n ==2:
        print("2")
    else:
        print(math.factorial(n)+1)
else:
    print(math.factorial(n) + math.factorial(m))

"""