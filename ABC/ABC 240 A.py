a, b = map(int, input().split())
if abs(a - b) == 1:
    print("Yes")
elif 10 in (a, b) and 1 in (a, b):
    print("Yes")
else:
    print("No")
