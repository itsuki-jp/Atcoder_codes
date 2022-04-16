n = int(input())
a = list(map(int, input().split()))
ans = [0] * n
for i in reversed(range(1, n + 1)):
    total = 0
    for j in range(i, n + 1, i):
        if ans[j - 1]:
            total += 1
    if a[i - 1] == total % 2:
        continue
    ans[i - 1] = 1
res = [_ + 1 for _ in range(n) if ans[_]]
print(len(res))
if len(res) != 0:
    print(*res)
