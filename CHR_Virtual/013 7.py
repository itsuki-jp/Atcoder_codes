from itertools import accumulate
n, c = map(int, input().split())
lst = [0] * (10 ** 5 + 10)
for _ in range(n):
    s, t, c = map(int, input().split())
    lst[s] += 1
    lst[t + 1] -= 1
acc = list(accumulate(lst))
print(max(acc))
