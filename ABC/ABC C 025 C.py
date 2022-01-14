import itertools

n, q = map(int, input().split())
lst = [0] * (n + 10)
for _ in range(q):
    l, r = map(int, input().split())
    lst[l] += 1
    lst[r + 1] -= 1
acc = list(itertools.accumulate(lst))
for j in acc[1:n + 1]:
    if j % 2 == 0:
        print(0, end="")
    else:
        print(1, end="")
print()
