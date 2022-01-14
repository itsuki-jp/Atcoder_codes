s = list(input())
if len(set(s)) == 1:
    exit(print(0))
alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']
ans = float("inf")
for A in alp:
    if A not in s:
        continue
    after = []
    before = s[::1]
    res = 0
    while list(set(after)) != [A]:
        after = []
        for i in range(len(before) - 1):
            if before[i] == A or before[i + 1] == A:
                after.append(A)
            else:
                after.append(s[i])
        res += 1
        before = after
    ans = min(res, ans)
print(ans)
