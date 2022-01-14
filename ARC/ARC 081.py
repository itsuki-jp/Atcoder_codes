import collections
n = int(input())
a = sorted(list(map(int, input().split())))

cnt = collections.Counter(a)
l1 = 0
l2 = 0

for i in cnt.keys():
    if cnt[i] >= 4:
        l1 = i
        l2 = i
    elif cnt[i] >= 2:
        l1, l2 = i, l1
print(l1 * l2)
