from itertools import permutations, combinations


def solve2( arr1 ):
    if len(arr1) == 2 * n:
        final.append(arr1)
    for i in range(2 * n - 1):
        if i in arr1:
            continue
        for j in lst[i]:
            res1 = arr1[::1]
            res1.append(j[0])
            res1.append(j[1])
            solve2(res1)
    pass


n = 3
comb = list(combinations(range(2 * n), 2))

lst = [[] for _ in range(2 * n - 1)]
final = []
for _ in comb:
    lst[_[0]].append(_)
print(*lst, sep="\n")
res = []
for _ in lst[0]:
    solve2(list(_))
print(*final, sep="\n")
lst = []


def solve( arr1, arr2 ):
    if len(arr2) == 1:
        lst.append(arr1)
    for nxt in arr2:
        res1 = arr1[::1]
        res1.append(nxt)
        res2 = arr2[::1]
        res2.remove(nxt)
        solve(res1, res2)
