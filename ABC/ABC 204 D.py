n = int(input())
t = list(map(int, input().split()))
total = sum(t)
lst = [0 for _ in range(total + 1)]
lst[0] = 1
for i in t:
    for j in range(total, -1, -1):
        if lst[j] == 1:
            lst[j + i] = 1
ans = total
for i in range(total//2 + 1):
    if lst[i] == 1:
        ans = i
print(total - ans)
