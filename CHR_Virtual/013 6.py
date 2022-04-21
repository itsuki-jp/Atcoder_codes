from itertools import accumulate

n, q = map(int, input().split())
lst = [0] * (n + 1)
for _ in range(q):
    l, r = map(int, input().split())
    lst[l - 1] += 1
    lst[r] -= 1
acc = list(accumulate(lst))
res = [_ % 2 for _ in acc]
print(*res[:-1], sep="")
