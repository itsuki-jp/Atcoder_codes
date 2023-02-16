n = int(input())
a = [int(_) - 1 for _ in input().split()]
idx_match = 0
for _ in range(n):
    if a[_] == _:
        idx_match += 1
ans = idx_match * (idx_match - 1) // 2

for i in range(n):
    j = a[i]
    if j < i == a[j] and j == a[i]:
        ans += 1
print(ans)
