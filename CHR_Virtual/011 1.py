x, y = map(int, input().split())
lst = [300000, 200000, 100000] + [0 for _ in range(1000)]
if x == y == 1:
    print(lst[0] * 2 + 400000)
else:
    print(lst[x - 1] + lst[y - 1])
