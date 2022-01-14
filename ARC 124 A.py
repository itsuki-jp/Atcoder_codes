n, k = map(int, input().split())
lst = [] * n
fixed = [0] * n
for i in range(k):
    ci, ki = input().split()
    ki = int(ki) - 1
    fixed[ki] = 1
    if ci == "L":
        lst.append([0] * ki + [1] * (n - ki))
    else:
        lst.append([1] * ki + [0] * (n - ki))

mod = 998244353
ans = 1
for i in range(n):
    if fixed[i]:
        continue
    cnt = 0
    for j in range(k):
        cnt += lst[j][i]
    ans = ans * cnt % mod
print(ans)