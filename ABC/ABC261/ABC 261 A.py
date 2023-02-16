l1, r1, l2, r2 = map(int, input().split())

lst = [0 for _ in range(200)]
for _ in range(r1 - l1):
    lst[l1 + _] += 1
for _ in range(r2 - l2):
    lst[l2 + _] += 1
print(lst.count(2))
