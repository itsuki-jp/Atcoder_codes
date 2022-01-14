a,b,c = map(int,input().split())
if c - b == b - a:
    print(0)
    exit()
if a == b == c:
    print(3)
elif a <= b < c:
