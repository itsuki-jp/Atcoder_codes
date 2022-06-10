v, a, b, c = map(int, input().split())
for _ in range(10**8):
    if v - a < 0:
        print("F")
        exit()
    elif v - a - b < 0:
        print("M")
        exit()
    elif v - a - b - c < 0:
        print("T")
        exit()
    v -= (a + b + c)
