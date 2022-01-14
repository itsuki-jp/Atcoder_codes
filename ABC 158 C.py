a, b, = map(int, input().split())

for i in range(1, 1000):
    price_a = 0.08 * i
    price_b = 0.1 * i

    if int(price_a) == a and int(price_b) == b:
        print(i)
        exit()
print(-1)
