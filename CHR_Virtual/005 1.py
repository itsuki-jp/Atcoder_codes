a = list(map(int, input().split()))
a.sort()
a,b,c = a
if c - b == b - a:
    print("Yes")
else:
    print("No")