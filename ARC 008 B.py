from math import ceil

n, m = map(int, input().split())
name = input()
kit = input()
kit_dict = {}
for i in kit:
    if i in kit_dict:
        kit_dict[i] += 1
    else:
        kit_dict[i] = 1
used = {}
for i in name:
    if i in used:
        used[i] += 1
    else:
        used[i] = 1
ans = 0
for i, j in zip(used.values(), used.keys()):
    if j in kit_dict:
        ans = max(ceil(i / kit_dict[j]), ans)
    else:
        exit(print(-1))
print(ans)
