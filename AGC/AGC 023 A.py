n = int(input())
A = list(map(int, input().split()))
d = {0:1}
num = 0
for a in A:
    num += a
    if num in d:
        d[num] += 1
    else:
        d[num] = 1
ans = 0
for v in d.values():
    if v > 1:
        ans += (v-1)*v // 2
print(ans)
