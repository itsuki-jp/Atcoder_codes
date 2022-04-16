s, c = map(int, input().split())
if s >= c // 2:
    print(c // 2)
else:
    print(s + (c - 2 * s) // 4)
