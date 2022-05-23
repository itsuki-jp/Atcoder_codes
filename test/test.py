n, a, b = list(map(int, input().split()))
total = 0
for i in range(1, n + 1):
    temp = i
    sum = 0
    d = 10
    while (i > 0):
        sum += i % d
        i //= d
        ######
    if a <= sum <= b:
        total += temp
print(total)
