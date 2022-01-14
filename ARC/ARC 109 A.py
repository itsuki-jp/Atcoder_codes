a, b, x, y = map(int, input().split())
if a == b:
    print(x)
elif a > b:
    num = a - b - 1
    print(min(num * y + x, num * 2 * x + x))
else:
    num = b - a
    print(min(num * y + x, num * 2 * x + x))
