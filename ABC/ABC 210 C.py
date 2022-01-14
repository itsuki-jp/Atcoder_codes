n, k = map(int, input().split())
c = list(map(int, input().split()))
temp = dict()
for i in range(k):
    if c[i] in temp:
        temp[c[i]] += 1
    else:
        temp[c[i]] = 1
ans = len(temp)
last = c[0]
for j in range(k, n):
    temp[last] -= 1
    if temp[last] == 0:
        del temp[last]
    if c[j] in temp:
        temp[c[j]] += 1
    else:
        temp[c[j]] = 1
    ans = max(ans, len(temp))
    last = c[j - k + 1]
print(ans)
