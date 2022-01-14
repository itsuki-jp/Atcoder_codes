a, b = map(int, input().split())
c, d = map(int, input().split())
x, y = abs(a - c), abs(b - d)

if (x, y) == (0, 0):
    print(0)
elif x == y or x + y <= 3:
    print(1)
elif (x + y) % 2 == 0 or x + y <= 6 or abs(x-y) <= 3:
    print(2)
else:
    print(3)
