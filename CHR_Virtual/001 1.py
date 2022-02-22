a,b = input().split()
if a * int(b) > b * int(a):
    print(b * int(a))
else:
    print(a * int(b))