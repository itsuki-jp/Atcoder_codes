from collections import Counter

n = int(input())
a = list(map(int, input().split()))
count = Counter(a)
mod = 10 ** 9 + 7
for i in range((n % 2 != 0) + 1, n, 2):
    if count[i] != 2:
        print(0)
        break
else:
    if n % 2 != 0 and count[0] != 1:
        print(0)
    else:
        print(pow(2, n // 2, mod))
